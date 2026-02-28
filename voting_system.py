# Functions : A Function is basically collection of code which is grouped togather to perform a specific task

# Array of Object : collection which store some data

# Data Types : data type of used to store diffrent type of data like booleans integers charachter and floating 

# Variable : A variable is like cotainer which store some data and to acess data

# Input : functions are used to take input from users

# 1 John 5400
# 2 Imran khan 7600
# 3 Trum 4500


#Funtion 1

def show_candidates(candidates):
   print("\n----- Candidates List----")
   for key , value in candidates.items():
      print(f"{key} , {value['name']} (votes :{value['votes']})")

def cast_vote(candidates):
   voter_name = input("Enter Your Name:")
   gender = input("Enter Your Gender (M/F): ").lower()

   if gender == "f":
      title = "Ms"
   elif gender == "m":
      title = "Mr"
   else:
      title = ""

   show_candidates(candidates)

   choice = input("Enter the Candidate Number to vote : ")

   if choice in candidates:
      candidates[choice]["votes"] += 1
      print(f"Thank you for vote {title} {voter_name}")
   else:
      print("Invalid Candidate Number ")



def show_results(candidates):
   print("------Voting Results-------")
   for c in candidates.values():
      print(f"{c['name']} - {c['votes']} votes")

candidates = {
    "1": {"name": "Alex", "votes": 0},
    "2": {"name": "John", "votes": 0},
    "3": {"name": "Nikolas", "votes": 0},
}

while True:
   print("1 .Cast vote:")
   print("2. Show Results")
   print("3. Exits")

   options = input("Enter your Option: ")

   if options == "1":
      cast_vote(candidates)
   elif options == "2":
      show_results(candidates)
   elif options == "3":
      print("Exiting the Program")
      break
   else: 
      print("You Have entered invalid Fuction")




