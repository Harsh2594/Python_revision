#Find Longest Word in a Sentence:
my_string = input("Enter a Sentence String ")

def longestWord(text):
  longest = ""
  word = ""
  i = 0
  length = len(text)
  while i < length:
    if text[i]!= " ":
      word += text[i]
    else:
      if len(word)>len(longest):
        longest = ""
        longest += word
        word = ""
      else:
        word = ""    
    i += 1  
#Dealing with last word in the sentence:    
  if len(word)>len(longest):
    longest = ""
    longest += word
    return longest
  else:
    return longest

print(longestWord(my_string))







longestWord(my_string)