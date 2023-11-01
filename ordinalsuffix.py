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


print(ordinalsuffix(int(input())))
