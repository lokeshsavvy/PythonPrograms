import datetime
now = datetime.datetime.now()
extract_date = lambda dt: (dt.year,dt.month,dt.day)
year, month, day = extract_date(now)
print(f'year: {year}')
print(f'month: {month}')
print(f'day: {day}')