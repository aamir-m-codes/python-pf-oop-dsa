"""
Datetime module is used in handling date and time related tasks. Some functions are explore below 
"""

import datetime


#   get the current date and time
date_time = datetime.datetime.now()
print(f'Date and Time: {date_time}')


# to get the number of particular day, starting from monday with number 1, tuesday number 2 and so on and so forth
day_number = datetime.datetime.now().isoweekday()
print(f'Number of Day: {day_number}')


# to get current date and time, in timestamp value
timestamp = datetime.datetime.now().timestamp()
print(f'Timestamp: {timestamp}')