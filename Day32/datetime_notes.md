# python datetime notes
```python
# import datetime class from datetime module
from datetime import datetime

# creating your own time object
date = datetime(year=2022, month=11, day=22)
print(date)


# get today date, you can also use datetime.today()
now = datetime.now()


# very self explanatory
now.day
now.month
now.year


# returns weekday in integer, if today is monday it will return 0, if it is sunday it will return 6
now.weekday()


# only get the date without time
now.date()




```