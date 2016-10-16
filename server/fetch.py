import os
import json
import re
import redis
import requests
import sys
from collections import OrderedDict
from math import ceil
from pprint import pprint
from random import randint
from time import time

ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN', '')
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)

BASE_URL = 'https://api.github.com/%s'
INF = float('Inf')
PAYLOAD = {'per_page': 100}
HEADERS = {
    'Authorization': 'token %s' % ACCESS_TOKEN,
    'User-Agent': 'https://github.com/kshvmdn/explore-github'}

s = requests.Session()
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def fetch_json(url, **kwargs):
    if 'payload' in kwargs:
        PAYLOAD.update(kwargs['payload'])

    if 'headers' in kwargs:
        HEADERS.update(kwargs['headers'])

    req = requests.Request('GET', url, headers=HEADERS,
                           params=PAYLOAD).prepare()

    key = ':'.join(filter(None, re.sub(r'\/|\?|=|&', ':', req.url).split(':')))
    print('KEY: %s' % key)

    value = r.get(key)

    if value is not None:
        print('FOUND')
        return json.loads(value.decode('utf-8'))

    value = s.send(req).json()
    r.set(key, json.dumps(value))
    r.expire(key, 60 * 60 * 24)
    return value


def get_paginated_results(url, n_results=INF, **kwargs):
    results = []
    seen = set()
    page_count = ceil(kwargs['count'] / PAYLOAD['per_page']) \
        if 'count' in kwargs else INF

    def get_page(page, **kwargs):
        seen.add(page)

        if 'randomize' in kwargs and kwargs['randomize'] and page_count != INF:
            while page in seen:
                page = randint(1, page_count + 1)

            return page

        return page + 1

    page = get_page(0, **kwargs)
    json = fetch_json(url, payload=dict(page=page))

    while json and len(json) > 0 and len(results) < n_results:
        results.extend(json)

        page = get_page(page, **kwargs)
        json = fetch_json(url, payload=dict(page=page))

    return results


def get_repo_stargazers(owner, repo):
    def get_stargazer_count():
        url = BASE_URL % ('repos/%s/%s' % (owner, repo))
        return fetch_json(url)['stargazers_count']

    endpoint = 'repos/%s/%s/stargazers' % (owner, repo)
    base = BASE_URL % endpoint

    stargazer_count = get_stargazer_count()

    results = get_paginated_results(base,
                                    n_results=min(200, stargazer_count),
                                    count=stargazer_count,
                                    randomize=True)

    return list(map(lambda r: r['login'], results))


def get_users_starred_repos(users):
    response = {}

    for user in users:
        endpoint = 'users/%s/starred' % user
        base = BASE_URL % endpoint

        results = get_paginated_results(base, n_results=100)

        for result in results:
            id_ = result['id']

            if id_ in response:
                response[id_]['count'] += 1
                response[id_]['users'] += [user]
                continue

            response[id_] = OrderedDict([
                ('id', result['id']),
                ('name', result['name']),
                ('owner', result['owner']['login']),
                ('description', result['description']),
                ('language', result['language']),
                ('fork', result['fork']),
                ('stargazers', result['stargazers_count']),
                ('watchers', result['watchers_count']),
                ('open_issues', result['open_issues_count']),
                ('forks', result['forks_count']),
                ('created_at', result['created_at']),
                ('updated_at', result['updated_at']),
                ('count', 1),
                ('users', [user])])

    return response


def fetch(owner, repo):
    if not (repo and owner):
        return None

    stargazers = get_repo_stargazers(owner, repo)
    repos = get_users_starred_repos(stargazers)

    return [json.loads(json.dumps(d), object_pairs_hook=OrderedDict)
            for d in repos.values()]

if __name__ == '__main__':
    start = time()

    r = fetch(*sys.argv[1:3])
    pprint(r)

    print('Finished in %fs.' % (time() - start))
