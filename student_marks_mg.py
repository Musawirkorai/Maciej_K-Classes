#DataType : 
#Array: is data storage tool in which we store the similar type of data 
#Conditional Statements :
#Functions:froup or bunch of code which is grouped togather to perform a specific task
#loops: are used to perform repeatitive tasks
#Float : is a type of data in which we store the fractional value like 12.54333 ans 54.6675999999999999999
#Append : is used to insert value or data inside the array
# Student Result Management System

students = []

def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "Fail"

def add_student():
    name = input("Enter student name: ")
    
    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))
    
    total = marks1 + marks2 + marks3
    average = total / 3
    grade = calculate_grade(average)
    
    student = {
        "Name": name,
        "Total": total,
        "Average": round(average, 2),
        "Grade": grade
    }
    
    students.append(student)
    print(" Student added successfully!\n")

def display_students():
    if not students:
        print("No students available.\n")
        return
    
    print("\n Student Records:")
    for s in students:
        print(f"Name: {s['Name']}, Total: {s['Total']}, "
              f"Average: {s['Average']}, Grade: {s['Grade']}")
    print()

# Main Program
while True:
    print("==== Student Result System ====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")