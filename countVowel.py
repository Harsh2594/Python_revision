#Count Vowels and Consonants:
string = input("Enter a string ")
vowel_count = 0
consonant_count = 0
for s in string:
  if s in ('a','e','i','o','u'):
    vowel_count = vowel_count+1
  elif s is " ":
    continue
  else:
    consonant_count = consonant_count+1  

print(f"{vowel_count} times vowel comes in this string")
print(f"Number of consonant count is {consonant_count}")
