#Check if a year is a leap year:
year = int(input("Enter any year to check leap year "))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")          