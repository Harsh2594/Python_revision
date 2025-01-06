#Remove Duplicates in a String
#Input: s = HappyNewYear
#Output: HapyNewYr
string = input("Enter a string").lower()
string_list = [(e) for e in string]
n = len(string_list)
for i in range(n):
  for j in range(i+1,n):
    if string_list[i] == string_list[j]:
      string_list[j] = ""
    else:
      continue
newString = ""    
for i in string_list:
  if i == " ":
    continue
  else:
    newString = newString+i

print(newString)