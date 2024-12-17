#Convert Celsius to Fahrenheit and vice versa.
temp = float(input("Enter Temparature in celsius "))

def celTofah(t):
  f = (t*(9/5))+32
  return f

print(f"Temparature in Fahrenheit is {celTofah(temp)}")