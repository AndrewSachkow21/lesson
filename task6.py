import datetime

first_date = datetime.datetime(year=int(input()), month=int(input()), day=int(input()))
second_date = datetime.datetime(year=int(input()), month=int(input()), day=int(input()))
interval = second_date - first_date
print(interval)