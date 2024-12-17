#Print Fibonacci sequence up to n terms.
n = int(input("How many terms of series you want to print. "))
a,b = 0,1
next_number = b
count = 1
while count < n:
  if count == 1:
    print(a,b,end=" ")
  else:
    print(next_number,end=" ")
    a = b
    b = next_number
    next_number = a + b
  count = count + 1

