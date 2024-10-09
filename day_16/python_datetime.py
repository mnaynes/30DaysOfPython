from datetime import datetime, date
now = datetime.now()
print(now)

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

new_year = datetime(year=2025, month=1, day=1)
days_left = new_year - now
print(days_left)

before = datetime(year=1970, month=1, day=1)
days_left = now - before
print(days_left)

# datetime module can be used to parse dates in data files, to display dates in various ways, etc
