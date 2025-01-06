#Calculate Power without Built-in Function:
number = int(input("enter a number "))
power = int(input("enter the power of above number "))

def calPower(num,p):
  n = 1
  answer = 1
  while n <= p:
    answer = answer*num
    n = n+1
  return answer

print(f"{number} and its power {power} is equal tp {calPower(number,power)}")
