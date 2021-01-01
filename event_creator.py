from datetime import datetime, timedelta
from cal_setup import get_calendar_service

def event_creator(Issue):
    service = get_calendar_service()

    # need golden hours finder, but this is ok for now
    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_body = eventify(Issue)

    event_result = service.events().insert(calendarId = 'primary', body = event_body).execute()


def eventify(Issue):
  # take Issue and make event
  d = datetime.now().date()
  tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
  start = tomorrow.isoformat()
  end = (tomorrow + timedelta(hours=1)).isoformat()
  event =  {
           "summary": "Today you're working on Github Issue #{}".format(Issue.id),
           "description": "Title: {} \n".format(Issue.title) + "Look at the issue on Github: {}".format(Issue.url),
           "start": {"dateTime": start, "timeZone": 'America/Los_Angeles'},
           "end": {"dateTime": end, "timeZone": 'America/Los_Angeles'},
  }
  return event
