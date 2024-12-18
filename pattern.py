#print (*) patterns
row = int(input("How many row you want "))
col = int(input("How many column you want "))

#pattern1:
for i in range(row):
  for j in range(i+1):
    print("*",end=" ")
  print()

print("------------------------------")
#pattern2:
for i in range(row):
  for j in range(row-i):
    print("*",end=" ")
  print()

print("-------------------------------")  

#pattern3:
for i in range(row):
  for j in range(row-i):
    print(" ",end=" ")
  for k in range(i+1):
    print("*",end=" ")
  print()    

print("--------------------------------")
#pattern4:
for i in range(5):
  for j in range(1,i+1):
    print(j,end=" ")
  print()    
