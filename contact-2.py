contact = {
    "Nawal": 733333333,
    "Shatha": 77777777,
    "raeefa": 8888888
}



def view ():
    # print(contact.items())
    for con in contact:
        print(con.title() + ' : '+ str(contact[con]))


def add ():
   n=  input("Enter name for added: ")
   p= input("Enter phone for added: ")
   contact.update({n:p})



def update ():
    key = input("Please, enter the name who you want to updat its number phone : ")
    ph = input("Ok. Now enter the updated phone number : ")
    contact[key] = ph




def delete ():
    dn = input("Please enter the name you want to deleted : ")
    del contact[dn]




print(" ***** LIST ***** \n 1. View the contact \n 2. Add new contact \n 3. Update contact \n 4. Delete contact \n 5. Exit ")


var = True
while var == True:
    numOperation = input("Enter number from above list of operation you want to perform it :  ")
    if numOperation == "1":
        view()
        # continue
    elif numOperation == "2":
        add()
    elif numOperation == "3":
        update()
    elif numOperation == "4":
        delete()
    elif numOperation == "5":
        break
    else:
        print("Error please enter number from the list ")
        break
