# variables :
#Array :
#conditionl Statement : 
# loops : 
#input functions :
# total balance :

Account_Holder_Name = "Alex "
balance = 10000
pin = "1234"

attempts = 0
max_attemps = 5




while attempts < max_attemps :
   print(f"Hello {Account_Holder_Name}")
   entered_pin = input("Enter your Pin : ")
   if entered_pin == pin:
      print("Login Succesfull")
      break
   else:
      attempts +=1
      print(f"Incorrect pin try again Attempt left : {max_attemps-attempts}")


if attempts == max_attemps:
   print("Card Blocked To Many incorrect Pin")
else: 
   while True:
      print("ATM Machine Main Menu ")
      print("1. Check Balance")
      print("2. Withdraw Money")
      print("3. Depsoit Money")
      print("4. Exit")

      choice = input("Enter the Choice : ")
      if choice == "1":
         print(f"Your Account Balance is ${balance}")
      elif choice =="2":
         amount = float(input("Enter the Amount to Withdraw: "))
         if amount >balance:
            print("Insufficient Balance ")
         else: 
            balance -= amount
            print(f"{amount} withdrawn Sucessfull")
      elif choice == "3":
         amount = float(input("Enter The Deposit Amount : "))
         balance +=amount
         print(f"${amount} Deposited Succesfully....!")
      elif choice == "4":
         print("Exiting The Program Thank you for using this ATM")
         break
      else : 
         print("Invlaid Choice try Again")


