my_list = list(map(int,input("Enter the list element separated by space").split()))

def maxNum(numList):
  max = numList[0]
  for e in numList:
    if e > max:
      max = e
    else:
      continue
  return max 

def minNum(numList):
  min = numList[0]
  for e in numList:
    if e < min:
      min = e
    else:
      continue
  return min

print(f"Maximum value in list is {maxNum(my_list)}\nMinimum value in list is {minNum(my_list)}")