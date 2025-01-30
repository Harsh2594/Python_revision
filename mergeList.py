#Merge Two Lists:
#1. without using any built-in funtion

my_list1 = list(input("Enter list element separated by space").split())
my_list2 = list(input("Enter list element separated by space").split())
merged_list = list()

def merged_two_list(list1,list2):
  print("method_1")
  for item in my_list1:
    merged_list.append(item)
  for item in my_list2:
    merged_list.append(item)
  return merged_list  

print(merged_two_list(my_list1,my_list2))

#2. Using '+' operator:
def merged_list_with_op(list1,list2):
  print("method_2")
  return list1+list2

print(merged_list_with_op(my_list1,my_list2))
