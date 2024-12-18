#Swap two variables without using a temporary variable.
a = int(input("Enter first number "))
b = int(input("Enter second number "))

a = a+b
b = a-b
a = a-b
print(f"value of a and b after swaping is {a}, {b}")

