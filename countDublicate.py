#Find Frequency of Characters:
my_string = input("Enetr a String").lower()
my_string_list = [(e) for e in my_string]
n = len(my_string_list)
for i in range(n):
  count = 1
  for j in range(i+1,n):
    if my_string_list[i] == " ":
      continue
    elif my_string_list[i] == my_string_list[j]:
      my_string_list[j] = " "
      count = count+1
  if count >1:
    print(f"Number of item {my_string_list[i]}: {count}")    
  else:
    pass
  