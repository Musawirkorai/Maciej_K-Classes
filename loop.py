number = int(input("Enter Any number : "))


print(f"\n Multiplication table of {number}")

for i in range (1 ,11):
   result = number * i
   print(f"{number} *{i} = {result}")

