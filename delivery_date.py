# Assignment D
# Customers often like to know when their orders are delivered, so we want to calculate an expected delivery date.
# We deliver orders within 1-2 work days in Denmark.
# If the order is placed before 15:00 (danish time) on a work day the customer can expect the package the following work day.
# If the order is placed on a non work day or after 15:00 it will be delivered after 2 work days.
# We are closed on Danish Public Holidays and in addition do not consider 5th of June (Constitution Day) and 31th of December (New Year’s Eve) as work days.
# Write a function that takes a datetime representing the time the order was placed and returns an expected delivery date.
# Notice the use of UTC timezone.
# Frederik Juhl Andreasen
# 2021-09-30
# Extra packages needed: Holidays, install with 'pip install holidays'
from datetime import date, timedelta, timezone, datetime
from zoneinfo import ZoneInfo
import holidays

dk_holidays = holidays.DK()
def get_delivery_date(order_date: datetime) -> datetime:
    # Function for checking if any day is a work day.
    def is_work_day(date: date) -> bool:
        # Check for weekends.
        if date.weekday() >= 5:
            return False
        # Check for holidays.
        if date in dk_holidays:
            return False
        # Check for New Year’s Eve.
        if date.month == 12 and date.day == 31:
            return False
        # Check for Constitution day.
        if date.month == 6 and date.day == 5:
            return False
        return True

    # Function for finding the next work day, by brute forcing one day at a time.
    def next_work_day(date: datetime) -> datetime:
        date += timedelta(days = 1)
        while not is_work_day(date):
            date += timedelta(days = 1)
        return date

    # Convert timezone.
    order_date = order_date.astimezone(ZoneInfo('Europe/Copenhagen'))

    # If order is placed on workday before 15 we deliver in one buisness day,
    # otherwise deliver in two buisness days.
    if is_work_day(order_date.date()) and order_date.time().hour < 15:
        return next_work_day(order_date).date()
    else:
        order_date = next_work_day(order_date)
        return next_work_day(order_date).date()
        


print(get_delivery_date(datetime(2021, 5, 20, 12, 51, 32, 199883, tzinfo=timezone.utc)))
# 2021-5-21
print(get_delivery_date(datetime(2021, 5, 20, 13, 3, 31, 245381, tzinfo=timezone.utc)))
# 2021-5-25
print(get_delivery_date(datetime(2020, 12, 29, 12, 15, 12, 0, tzinfo=timezone.utc)))
# 2020-12-30
print(get_delivery_date(datetime(2020, 12, 29, 14, 15, 12, 0, tzinfo=timezone.utc)))
# 2021-1-4
