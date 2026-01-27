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

