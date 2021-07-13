from datetime import datetime, date, time, timezone

nowutc = datetime.now(timezone.utc)
print(nowutc)
print(nowutc.date())
print(date(2000, 1, 1))
