import requests

API_URL = 'https://api.github.com/users/{}/repos'


def main(user):
    return parse(request(user))


def request(user):
    ''' return the response body for the url with the given'''
    return requests.get(url=API_URL.format(user))


def parse(response):
    repos = response.json()
    data = []
    if repos is None:
        return None
    for repo in repos:
        if 'name' in repo and not repo['fork']:
            data.append({
                'name': repo['name'],
                'desc': repo['description'],
                'lang': repo['language'],
                'stars': repo['stargazers_count'],
                'dates': {
                    'created': repo['created_at'],
                    'updated': repo['updated_at'],
                    'pushed': repo['pushed_at']
                }
            })
    return data

if __name__ == '__main__':
    import pprint
    u = 'kshvmdn'
    pprint.pprint(get_data(u))
