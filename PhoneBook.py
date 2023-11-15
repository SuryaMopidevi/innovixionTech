# initialising dictionary for collecting data
contact={}

# adding contact 
def addContact():
    name=input("Enter contact name : ")
    Email=input("Enter email : ")
    address=input("Enter address : ")
    phoneNumber=int(input("Enter phone number : "))
    contact[name]={
        'Email': Email,
        'PhoneNumber': phoneNumber,
        'Address': address
    }
    print(f"{name} is added to contact list")

# viewing contact 
def viewContact():
    if not contact:
        print("Your contact list is empty ")
    else:
        for name in contact.keys():
            print(f"{name} contact details : ")
            # print(f"Email : {contact[name]['Email']}")
            # print(f"Phone Number : {contact[name]['PhoneNumber']}")
            # print(f"Address : {contact[name]['Address']}")
            print(contact[name])


# searching contact based on contact name
def searchContact():
    name=input("enter contact name to search : ")
    if not contact:
        print("Empty contact list")
    elif name not in contact.keys():
        print("Contact not found ")
    else:
        for na in contact.keys():
            if na == name :
                print(f"{name} contact details : ")
                print(f"Phone Number : {contact[name]['PhoneNumber']}")
                print(f"Address : {contact[name]['Address']}")
                print(f"Email : {contact[name]['Email']}")

# updating contact based on contact name 
def updateContact():  
    name=input("enter contact name to update : ")
    if not contact:
        print("contact list s empty")
    elif name not in contact:
        print("Contact not found ")
    else:
        print("p:phone number")
        print("e:email")
        print("a:address")
        update=input("enter field(p/e/a) to be updated :").lower()
        # updating phone number 
        if update=='p':
            ph=int(input("enter phone number to update : "))
            contact[name]['PhoneNumber']=ph
            # 'PhoneNumber': ph
            # }
            print(f"{name}'s Phone number : {contact[name]['PhoneNumber']} is updated...")

        # updating address
        elif update=='a':
            ad=input("enter address to update : ")
            contact[name]['Address']=ad
            print(f"{name}'s  address : {contact[name]['Address']} is updated...")

        # updating email
        elif update=='e':
            em=input("enter email to update : ")
            contact[name]['Email']=em
            print(f"{name}'s Email : {contact[name]['Email']} is updated...")
        else:
            print("Error due to invalid input")
            print(f"{name} contact list is not updated...")

# deleting contact 
def deleteContact():  
    name=input("enter contact name to delete : ")
    if not contact:
        print("contact list is empty")
    elif name not in contact:
        print("Contact not found ")
    else:
        del contact[name]
        print(f"{name} contact list is deleted... ")


while(True):
    print("welcome to contact management system ")
    print("a.Add contact")
    print("v.View contact")
    print("u.Update contact")
    print("s.Search contact")
    print("d.Delete contact")
    print(" press any other keys for Exit")
    
    # chooosing operation
    operation=input("Choose operation : ").lower()

    # checking the operation 
    if operation=='a' :
        addContact()
    elif operation == 'v' :
        viewContact()
    elif operation == 'u' :
        updateContact()
    elif operation == 's' :
        searchContact()
    elif operation == 'd' :
        deleteContact()
    else :
        print("Invalid operation ")
        break
print("Thank you ! Have a good day ..... ")
