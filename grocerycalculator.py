#Array : to use and store the data of the items

#Loop : calculate and get input of multiple items

#variable : varible wil be used to store results
#conditional statements : to chek the diffrent coditions we may use the conditional statement
#input : input for the taking data from the user
# print : to display outputs
# Grocery Bill Calculator

items = []
total = 0

print(" Welcome to Grocery Store")

while True:
    name = input("\nEnter item name (or type 'done' to finish): ")
    
    if name.lower() == 'done':
        break

    price = float(input("Enter item price: "))

    items.append((name, price))
    total += price

print("\n Your Bill:")
print("----------------------")

for item in items:
    print(f"{item[0]} : Rs {item[1]:.2f}")

print("----------------------")
print(f"Total Amount: Rs {total:.2f}")

print("\nThank you for shopping!")