#Print all prime numbers in a given range.

n1 = int(input("Enter start point"))
n2 = int(input("Enter End point"))

for i in range(n1+1,n2):
  j=2
  while j <= (i//2):
    if i%j==0:
      break
    j = j+1
  else:
    print(i,end=" ")  
  i = i+1
