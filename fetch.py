import os
import json
import requests
from collections import OrderedDict
from pprint import pprint


BASE_URL = 'https://api.github.com/%s?page=%s&per_page=100'


def fetch_json(url):
    headers = {
        'User-Agent': 'https://github.com/kshvmdn/discover-github'
    }

    payload = {
        'client_id': os.environ.get('CLIENT_ID', None),
        'client_secret': os.environ.get('CLIENT_SECRET', None)
    }

    return requests.get(url, headers=headers, params=payload).json()


def get_repo_stargazers(owner, repo):
    users = []

    endpoint = 'repos/%s/%s/stargazers' % (owner, repo)

    page = 1
    json = fetch_json(BASE_URL % (endpoint, page))

    while json and len(json) > 0:
        users.extend(u['login'] for u in json)

        if len(json) < 100:
            break

        page += 1
        json = fetch_json(BASE_URL % (endpoint, page))

    return users


def get_users_starred_repos(users, repos=None):
    if not repos:
        repos = dict()

    for user in users:
        endpoint = 'users/%s/starred' % user

        page = 1
        json = fetch_json(BASE_URL % (endpoint, page))

        while json and len(json) > 0:
            for r in json:
                if r['id'] not in repos:
                    repos[r['id']] = OrderedDict([
                        ('id', r['id']),
                        ('name', r['name']),
                        ('owner', r['owner']['login']),
                        ('slug', r['full_name']),
                        ('description', r['description']),
                        ('stargazers_count', r['stargazers_count']),
                        ('watchers_count', r['watchers_count']),
                        ('fork_count', r['forks_count']),
                        ('language', r['language']),
                        ('starred_by', [user]),
                        ('count', 1)
                    ])
                else:
                    repos[r['id']]['count'] += 1
                    repos[r['id']]['starred_by'].append(user)

            if len(json) < 100:
                break

            page += 1
            json = fetch_json(BASE_URL % (endpoint, page))

    return repos


def main(owner, repo, depth=1):
    if not owner or not repo:
        return None

    repos = get_users_starred_repos(get_repo_stargazers(owner, repo))

    while depth > 1:
        for repo_id, repo in repos.items():
            repo_owner, repo_name = repo['slug'].split('/')
            repos = get_users_starred_repos(
                        get_repo_stargazers(repo_owner, repo_name), repos)

        depth -= 1

    return [json.loads(json.dumps(d), object_pairs_hook=OrderedDict)
            for d in repos.values()]

if __name__ == '__main__':
    pprint(main('kshvmdn', 'kshvmdn.github.io'))
