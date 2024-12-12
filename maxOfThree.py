#Find the maximum and minimum of three numbers.
a = int(input("Enter first number a = "))
b = int(input("Enter second number b = "))
c = int(input("Enter third number c = "))

def max(x,y,z):
  if a>b:
    if a>c:
      print("Max of three number is ",a) 
    else:
      print("Max of three number is ",c) 
  else:
    if b>c:
      print("Max of three number is ",b)
    else:
      print("Max of three number is ",c) 
  
def min(x,y,z):
  if a<b:
    if a<c:
      print("min of three is ",a)
    else:
      print("Min of three is ",c)
  else:
    if b<c:
      print("min of three is ",b)
    else:
      print("min of three is ",c)  

max(a,b,c)
min(a,b,c)