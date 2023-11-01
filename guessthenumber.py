import math
import random


#define the ordinal of the number
def ordinalsuffix(num):
  if num % 100 in (11, 12, 13):
    return str(num) + 'th'
  elif num % 10 == 1:
    return str(num) + 'st'
  elif num % 10 == 2:
    return str(num) + 'nd'
  elif num % 10 == 3:
    return str(num) + 'rd'
  else:
    return str(num) + 'th'


# get inputs from the users
upper = int(input("Enter the upper bound : "))
lower = int(input("Enter the lower bound : "))
#get the number of chances
chances = round(math.log(upper - lower + 1, 2))
# get the random number with the range
x = random.randint(lower, upper)
print("You have only ", chances, " number of chances")
count = 0
#loop the chances
while count < chances:
  count += 1
  #countOrdinal=ordinalsuffix(count)
  guess = int(input("Enter your guess : "))
  if x == guess:
    print("Congratulations! you have done it on your ", ordinalsuffix(count),
          " try")
    break
  elif x > guess:
    print("Your guess is smaller than the number")
  elif x < guess:
    print("Your guess is higher than the number")
  if count >= chances:
    print("Better luck next time. The number is ", x)
