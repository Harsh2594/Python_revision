#Count Words in a Sentence:
my_string = input("Enter a Sentence String ")

def countWords(text):
  length = len(my_string)
  word = ""
  i = 0
  count = 0
  if length > 0:
    while i < length:
      if text[i] != " ":
        word += text[i]
      else:
        if len(word)>1:
          count += 1
      i += 1    
    return count+1 
  else:
    return 0         

print(f"Number of words in given sentence are {countWords(my_string)}")  