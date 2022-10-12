def leap(year):
    if year%4 == 0:
        # more conditions to check
        if year%100 == 0 and year%400 != 0:
            return False
        else:
            return True
    else:
        # not a leap year
        return False


def days_in_month(year,month):
    if month>12 or month<1:
        return 'Invalid month'

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap = leap(year)

    if month==2 and is_leap:
        return 29
    else:
        return month_days[month-1]




year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
days = days_in_month(year, month)
print(days)

