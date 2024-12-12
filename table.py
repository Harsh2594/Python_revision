#Print the multiplication table of a number.
a = int(input("Enter the number to print its table "))
for i in range(1,11):
  print(f"{a}*{i} = {a*i}")
