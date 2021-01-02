import datetime
from datetime import date
import calendar

def findDay(date):
    year, month, day = (int(i) for i in date.split('-'))
    born = datetime.date(year, month, day)
    return born.strftime("%A")


date = '2020-12-11'
print(findDay(date))
