#Find the factorial of a number using a loop.
n = int(input("Enter the any number to find its factorial "))
fac = 1
while n >= 1:
  fac = fac*n 
  n = n-1
print(f"factorial of given number is {fac}")  

#Factorial using for loop
num = int(input("Enter the Number for Calculating factorial"))
fact=1
for i in range(num):
    fact = fact*num
    num -= 1
print(fact)

#factorial using recursion
num = int(input("Enter the Number for Calculating factorial"))
def factorial(n):
   if n==1:
      return
   return factorial(n-1)*n

print(factorial(num))