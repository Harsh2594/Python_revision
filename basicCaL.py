#Create a program to add, subtract, multiply, and divide two numbers.
def add(a,b):
  sum = a+b
  return sum
def sub(a,b):
  diff = a-b
  return diff
def multi(a,b):
  prod = a*b
  return prod

print("Make addition operation")
addition = add(int(input("a = ")),int(input("b = ")))
print("Sum of two numbers is ",addition)

print("Make subtraction operation")
subtraction = sub(int(input("a = ")),int(input("b = ")))
print("difference of two numbers is ",subtraction)

print("Make multiplication operation")
multiplication = multi(int(input("a = ")),int(input("b = ")))
print("product of two numbers is ",multiplication)