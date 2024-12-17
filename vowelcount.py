#Count the number of vowels in a string.
st = input("Enter the string ")
lstOfvowel = ['a','e','i','o','u']
count = 0
for s in st:
  if s in lstOfvowel:
    count = count + 1

print("Number of vowel is ",count)