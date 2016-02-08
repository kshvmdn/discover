import requests

api = 'https://api.github.com/users/{}/repos'

repos = data = requests.get(url=api.format('kshvmdn')).json()

for repo in repos:
    print(repo['name'])
