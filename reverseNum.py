#Reverse any given number:
n = int(input("Enter any number to find reverse of it. "))

def reverse_Num(number):
  reversed_number = 0
  while number > 0:
    last_digit = number%10
    reversed_number = reversed_number*10 + last_digit
    number = number // 10
  return reversed_number

print(f"Rverse of given number is {reverse_Num(n)}")  
  
