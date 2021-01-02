import requests
import os
from pprint import pprint
import json
from event_creator import event_creator
import datetime

class Activity:
    def __init__(self, type="", created_at=""):
        self.type = type
        self.created_at = created_at
    def __str__(self):
        return "Activity: (type=%s, created_at=%s)" %(self.type, self.created_at)

parsedActivities =[]
def parse_activity(activity):
    # print(issue["due_on"])
    # print(type(issue))
    currentActivity = Activity(activity["type"], activity["created_at"])

    parsedActivities.append(currentActivity)

token = os.getenv('GITHUB_TOKEN', '5e39dfbc77dfefeeba683988620561bcadef65ad')
owner = "tabbykatz"
query_url = f"https://api.github.com/users/{owner}/events"
params = {
    "per_page": "100",
}
headers = {'Authorization': f'token {token}'}
r = requests.get(query_url, headers=headers, params=params)

activities = json.loads(r.text)

for activity in activities:
    # print(issue)
    # print("\n")
    parse_activity(activity)
for activity in parsedActivities:
    print(activity)

# look at github activity (commits, prs, code review, etc) and define a set of golden work hours.
# exclude weekends?
# what about conflicts in the calendar?

#events api/ PushEvents have time created. an array of dicts.[array][type]: PushEvent, [array][created_at]: timestamp
  # [
  # {
  #   "id": "14622142418",
  #  --> "type": "PushEvent",
  #   "actor": {
  #     "id": 55110763,
  #     "login": "tabbykatz",
  #     "display_login": "tabbykatz",
  #     "gravatar_id": "",
  #     "url": "https://api.github.com/users/tabbykatz",
  #     "avatar_url": "https://avatars.githubusercontent.com/u/55110763?"
  #   },
  #   "repo": {
  #     "id": 317580762,
  #     "name": "tabbykatz/holbertonschool-web_front_end",
  #     "url": "https://api.github.com/repos/tabbykatz/holbertonschool-web_front_end"
  #   },
  #   "payload": {
  #     "push_id": 6247022224,
  #     "size": 1,
  #     "distinct_size": 1,
  #     "ref": "refs/heads/main",
  #     "head": "e5e502318c79a635e216ab7a18cc5a9429cb22a1",
  #     "before": "5001629a2e397f63e0b1c90f8479b58f9c9df7d8",
  #     "commits": [
  #       {
  #         "sha": "e5e502318c79a635e216ab7a18cc5a9429cb22a1",
  #         "author": {
  #           "email": "tomelay@gmail.com",
  #           "name": "tabbykatz"
  #         },
  #         "message": "task 13",
  #         "distinct": true,
  #         "url": "https://api.github.com/repos/tabbykatz/holbertonschool-web_front_end/commits/e5e502318c79a635e216ab7a18cc5a9429cb22a1"
  #       }
  #     ]
  #   },
  #   "public": true,
  # -->  "created_at": "2020-12-22T23:21:55Z"
  # },
  # ]
