#Check if a number is prime.

n = int(input("Enetr a number"))
i=2
while i <= (n//2):
  if n%i == 0:
    print("Not Prime")
    break
  i = i+1
else:
  print("Prime")