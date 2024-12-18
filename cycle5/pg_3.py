
import datetime
today=datetime.datetime.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print("Yesterday=",yesterday.date())
print("Today=",today.date())
print("Tomorrow=",tomorrow.date())
