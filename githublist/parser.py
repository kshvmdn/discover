import requests
import collections

API_URL = 'https://api.github.com/users/{}/repos'


def main(user):
    return parse(request(user))


def request(user):
    return requests.get(url=API_URL.format(user))


def parse(response):
    repos = response.json()
    data = []
    if repos is None:
        return None
    for repo in repos:
        if 'name' in repo and not repo['fork']:
            star_str = 'star' if repo['stargazers_count'] == 1 else 'stars'
            data.append(collections.OrderedDict(
                [('name', repo['name']),
                 ('desc', repo['description']),
                 ('lang', repo['language']),
                 ('stars', repo['stargazers_count']),
                 ('star_str', star_str)]))
    return data


if __name__ == '__main__':
    import pprint
    u = 'kshvmdn'
    pprint.pprint(main(u))
