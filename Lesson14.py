import sys

def intitial_phonebook():
    rows, cols = int(input("Enter number of contacts: ")), 5
    phonebook = []
    print(phonebook)
    for i in range(rows):
        print("\nEnter contact %d details in the following order(ONLY):" % (i+1))
        print("NOTE: * indicates mandatory field")

        print("....................................................................")        
        temp = [] 
    for j in range(cols):    
        if j == 0:
            temp.append(str(input("Enter Name*: ")))
            if temp[j] == "":
                sys.exit("Name is a mandatory field. Exiting program due to blank field")
        if j == 1:
             temp.append(str(input("Enter Number: ")))


        if j == 2:
             temp.append(str(input("Enter Email ID: ")))
             if temp[j] == "" or temp[j] == " ":
                 temp[j] = "None"

        if j == 3:
             temp.append(str(input("Birthday (DD/MM/YYYY): ")))
             if temp[j] == "" or temp[j] == " ":
                 temp[j] = "None"
        if j == 4:
             temp.append(str(input("Enter category (Family/Friends/Work/Others): ")))
             if temp[j] == "" or temp[j] == " ":
                 temp[j] = "None"

        phonebook.append(temp)
    print(phonebook)
    return phonebook

def menu():
    print("**************************************************************************")
    print("\t\t\tPHONEBOOK Directory", flush = False)
    print("**************************************************************************")
    print("\tyou can now perform the following operations in the phone book\n")
    print("1.Add new contact")
    print("2.Delete an existing contact")
    print("3.Delete all contacts")
    print("4.Search for a contact")
    print("5.Display all contacts")
    print("6.Exit Phonebook")

    choice = int(input("Please enter your choice:"))
    return choice

def add_contact(phonebook):

    dip = []
    for i in range(len(phonebook[0])):

        if i == 0:
            dip.append(str(input("Enter Name*: ")))
        if i == 1:
            dip.append(str(input("Enter Number: ")))      
        if i == 2:
            dip.append(str(input("Enter Email ID: ")))        
        if i == 3:
            dip.append(str(input("Enter Birthday (DD/MM/YYYY): ")))         
        if i == 4:
            dip.append(str(input("Enter category (Family/Friends/Work/Others): ")))        

    phonebook.append(dip)
    return phonebook

def remove_exicting(pb):

    query = str(input("Enter the name of the contact to be deleted: "))
    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1 
            print(pb.pop(i))
            print("This query has been now removed")
            return pb
    if temp == 0:
        print("No such contact found")
        return pb
def remove_all(pb):
    return pb.clear()

def search_existing(pb):
    choice = int(input("Enter search criteria\n\n1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\nPlease enter:")) 

    temp = []
    check = -1

    if choice == 1:
        query = str(input("Enter the name of the contact to be searched: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
        query = str(input("Enter the number of the contact to be searched: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])

            else:
                print("No such contact found")
                return -1
            if check == -1:
                return -1
            else:
                display_all(temp)
                return check
def display_all(pb):
    if not pb:
        print("Phonebook is empty")
    else:
        for i in range(len(pb)):
            print (pb[i])
def Thanks():
    print("**************************************************************************")
    print("Thank you for using our Phonebook Directory")
    print("Please visit again")
    print("**************************************************************************")
    sys.exit("GoodBye Have a nice day ahead!")

print("...........................WELCOME TO PHONEBOOK DIRECTORY.........................")
print("Hello dear user ! Let's set up your phonebook")
print("You may not visit the dictionary")
print("..................................................................................")

ch = 1
pb = intitial_phonebook()

while ch in (1,2,3,4,5,6):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_exicting(pb)
    elif ch == 3:
        pb = remove_all(pb)
    elif ch == 4:
        search_existing(pb)
    elif ch == 5:
        display_all(pb)
    elif ch == 6:
        Thanks()
        if d  == -1:
            print("No such contact found")

        else:
            Thanks()    
