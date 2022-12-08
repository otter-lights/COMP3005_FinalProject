import sqlite3
connection = sqlite3.connect('project.db');
connection.execute("PRAGMA foreign_keys = 1;");
crsr = connection.cursor();


logged_in = False
is_admin = False

def browse():
    print("Browsing the Collection...")

def login():
    email = input("Email: ")
    password = input("Password: ")
    crsr.execute("SELECT uid, password, is_admin FROM USER_TABLE WHERE email=?", (email,))
    ans = crsr.fetchone()
    print(ans)
    if(not ans):
        print("No account exists with that email.\nReturning to menu...")
        return(False)
    elif(ans[1] == password):
        print("Logging In...")
        if(ans[2] == 1):
            return(ans[0], True)
        else:
            return(ans[0], False)
    else:
        print("Incorrect password. \nReturning to menu...")
        return(False)

def createaccount():
    print("Creating Account...")

def viewcart():
    print("Viewing Cart...")

def viewreports():
    print("Viewing Reports...")

while(True):
    print("\nWelcome to TheBookStore.\nPlease choose an option from the following menu: ")
    if(logged_in != False and is_admin == False):
        option = input(" (1) Browse Our Collection \n (2) View Cart \n (3) Exit Store \n")
        if(option == "1"):
            browse()
        elif(option == "2"):
            viewcart()
        elif(option == "3"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;
    elif(logged_in != False and is_admin == True):
        option = input(" (1) Browse Our Collection \n (2) View Reports \n (3) Exit Store \n")
        if(option == "1"):
            browse()
        elif(option == "2"):
            viewreports()
        elif(option == "3"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;
    else:
        option = input(" (1) Browse Our Collection \n (2) View Cart \n (3) Log In \n (4) Create a New Account \n (5) Exit Store \n")
        #print(option)
        if(option == "1"):
            browse()
        elif(option == "2"):
            viewcart()
        elif(option == "3"):
            logged_in, is_admin = login()
        elif(option == "4"):
            createaccount()
        elif(option == "5"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;

connection.close();
