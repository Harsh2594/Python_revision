#Replace Words in a String:
#Input: text = "I love apples and apples are tasty." replace all apple with orange
#Output:"I love orange and orange are tasty."

my_string = input("Enter a string ")
old_word = input("Enter word that you want to replace ")
new_word = input("Enter new word ")

def replace_all(my_string,old_word,new_word):
  word = ''
  result = ''
  length = len(my_string)
  i = 0
  while i < length:
    if my_string[i] != " ":
      word += my_string[i]
    else:
      if word == old_word:
        result += new_word
      else:
        result += word
      result += ' '
      word = ''
    i += 1  
  
  if word == old_word:
    result += new_word
  else:
    result += word

  return result    
           
print(replace_all(my_string,old_word,new_word))