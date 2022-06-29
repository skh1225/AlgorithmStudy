from datetime import datetime, timedelta

t = datetime.strptime('23:11', '%H:%M')+timedelta(minutes=10)
print(t.hour)
