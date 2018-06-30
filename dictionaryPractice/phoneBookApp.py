phoneBook = {
    "Justin" : "281-755-9979",
    "Jeanne" : "281-543-9934",
    "Jessica" : "936-336-0396"
    } 

def choice1():
    name = input("Enter Name: ")
    print("Found entry for {}: {}".format(name, phoneBook[name]))

def choice2():
    name = input("Enter Name: ")
    number = input("Enter Phone Number: ")
    phoneBook[name] = number
    print("Entry added for {}".format(name))

def choice3():
    name = input("Enter Name: ")
    del phoneBook[name]
    print("Deleted entry for {}".format(name))

def choice4():
    print(phoneBook)

def choice5():
    print("Bye!")

print("Electronic Phone Book \n =====================\n 1. Look up an entry \n 2. Set an entry \n 3. Delete an entry \n 4. List all entries \n 5. Quit")
choice = input("What would you like to do? Select 1-5 ")

if choice == "1":
     print(choice1())
elif choice == "2":
    print(choice2())
elif choice == "3":
    print(choice3())
elif choice == "4":
    print(choice4())
elif choice == "5":
    print(choice5())
else:
    print("Invalid choice")


