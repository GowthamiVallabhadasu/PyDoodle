#importing date time module
from datetime import datetime

#import pytz
#datetime is a class present in date time module, now is a method in date time class
#now function returns the current date time value
currentTime = datetime.now()
print("Current time at green wich mean time raw format is  - ", currentTime)
#printing the attributes of now()
print("current month is ", currentTime.month)
print("current date is ", currentTime.year)
print("current day is ", currentTime.day)
print("current hour is ", currentTime.hour)
print("current minute is ", currentTime.minute)
print("current second is ", currentTime.second)
print("current millisecond is ", currentTime.microsecond)

# now() accepts timezone as parameter. But needs pytz module to pass time zone parameter but in the IDE,this module is not presen

#using strftime method to manipulate da e time.
print(currentTime.strftime("%Y-%m-%d %H:%M:%S"))
