#Remove dublicate element from list:
my_list = input("Enter the list element separated by space ").split()
new_list = list()
n = len(my_list)

for e in my_list:
  if e not in new_list:
    new_list.append(e)
  else:
    continue
print(new_list)    


 
# for i in range(n):
#   for j in range(i+1,n):
#     if my_list[i] == my_list[j]:
#       my_list[j] = " "
#     else:
#       continue  
#   if my_list[i] != " ":
#     new_list.append(my_list[i])
#   else:
#     pass

# print(new_list)