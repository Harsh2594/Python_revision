#Title Case String:
#INPUT: harsh Pratap singh
#Output: Harsh Pratap Singh

my_string = input("Enter a string ")
my_string_list = [(e) for e in my_string]
n = len(my_string_list)
my_string_titleCase = ""
for i in range(n):
  if i == 0:
    my_string_list[i] = my_string_list[i].upper()
  elif my_string_list[i] == " ":
    my_string_list[i+1] = my_string_list[i+1].upper()
  elif my_string_list[i-1] == " ":
    pass  
  else:
    my_string_list[i] = my_string_list[i].lower()
    

for e in my_string_list:
  my_string_titleCase = my_string_titleCase+e

print(my_string_titleCase)
