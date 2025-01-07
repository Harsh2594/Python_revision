#Check Substring Presence:
my_string = input("Enter a string ")
my_sub_string = input("Enter Substring ")
#Without using any built-in method:
def custom_find(my_string,my_sub_string,start=0,end=None):
  if end is None:
    end = len(my_string)
  for i in range(start,(end-len(my_sub_string)+1)):
    if my_string[i:i+len(my_sub_string)] == my_sub_string:
      return i  
  return -1

print(f"Sub string {my_sub_string} is presence at index {custom_find(my_string,my_sub_string)}")  




#Using the 'in' keyword

if my_sub_string in my_string:
  print(f"{my_sub_string} is presence")
else:
  print(f"{my_sub_string} is not presence")  

#Using find() method:

if my_string.find(my_sub_string) != -1:
  print(f"{my_sub_string} is presence")
else:
  print(f"{my_sub_string} is not presence")


#Using index() method:

try:
  my_string.index(my_sub_string)
  print(f"{my_sub_string} is presence")
except ValueError:
  print(f"{my_sub_string} is not presence")    
