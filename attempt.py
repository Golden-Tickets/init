import requests
import os
from pprint import pprint

token = os.getenv('GITHUB_TOKEN', 'dbd4a4a9f0938dad2f43b5ceb19bef72f6e16c98')
owner = "Golden-Tickets"
repo = "init"
query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
params = {
    "state": "open",
}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)
pprint(r.json())
