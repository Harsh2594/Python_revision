st = input("Enter any string which you want to reverse ")
lst = list()
for s in st:
  lst.append(s)
print(lst)  
st1 = str()
n = len(lst)
while n > 0:
  st1 = st1 + lst[n-1]
  n = n-1

print(f"Reverse string is {st1}")  