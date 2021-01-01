# look at github activity (commits, prs, code review, etc) and define a set of golden work hours.
# exclude weekends?
# what about conflicts in the calendar?

#events api/ PushEvents have time created. an array of dicts.[array][type]: PushEvent, [array][created_at]: timestamp
  [
  {
    "id": "14622142418",
   --> "type": "PushEvent",
    "actor": {
      "id": 55110763,
      "login": "tabbykatz",
      "display_login": "tabbykatz",
      "gravatar_id": "",
      "url": "https://api.github.com/users/tabbykatz",
      "avatar_url": "https://avatars.githubusercontent.com/u/55110763?"
    },
    "repo": {
      "id": 317580762,
      "name": "tabbykatz/holbertonschool-web_front_end",
      "url": "https://api.github.com/repos/tabbykatz/holbertonschool-web_front_end"
    },
    "payload": {
      "push_id": 6247022224,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/main",
      "head": "e5e502318c79a635e216ab7a18cc5a9429cb22a1",
      "before": "5001629a2e397f63e0b1c90f8479b58f9c9df7d8",
      "commits": [
        {
          "sha": "e5e502318c79a635e216ab7a18cc5a9429cb22a1",
          "author": {
            "email": "tomelay@gmail.com",
            "name": "tabbykatz"
          },
          "message": "task 13",
          "distinct": true,
          "url": "https://api.github.com/repos/tabbykatz/holbertonschool-web_front_end/commits/e5e502318c79a635e216ab7a18cc5a9429cb22a1"
        }
      ]
    },
    "public": true,
  -->  "created_at": "2020-12-22T23:21:55Z"
  },
  ]
