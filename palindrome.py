#Check if a string is a palindrome.
st = input("Enter the string ")
#create a empty string:
st1 = ""
#loop through original string and reverse it:
for c in st:
  st1 = c + st1

if st == st1:
  print("palindrome")
else:
  print("not palindrome")  
