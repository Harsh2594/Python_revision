#Find Second Largest Number in a List:
my_list = list(map(int,input("Enter the list element separated by space ").split()))
n = len(my_list)
for i in range(n):
  for j in range(0,n-i-1):
    if my_list[j]>my_list[j+1]:
      my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    else:
      continue  

print(f"Sorted list in ascending order is {my_list}")
print(f"Second largest element in the list is {my_list[-2]}")