#Find the maximum and minimum of three numbers.
a = int(input("Enter first number a = "))
b = int(input("Enter second number b = "))
c = int(input("Enter third number c = "))

#use built-in Python functions for simplicity:
maximum = max(a,b,c)
minimum = min(a,b,c)

print("max of three numbers is ",maximum)
print(f"min of three numbers is {minimum}")
