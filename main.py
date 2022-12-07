#import sqlite3
#connection = sqlite3.connect('project.db');
#connection.execute("PRAGMA foreign_keys = 1;");

while(True):
    option = input("Welcome to TheBookStore.\n Please choose an option from the following menu: \n (1) Browse Our Collection \n (2) Log In \n (3) Create a New Account \n (4) Exit Store \n")
    #print(option)
    if(option == "1"):
        print("Browsing the Collection...")
    elif(option == "2"):
        print("Logging In...")
    elif(option == "3"):
        print("Creating Account...")
    elif(option == "4"):
        print("Exiting Program ...")
        break;
    else:
        print("Sorry, we didn't understand that input. Please choose from the options below: ")
        continue;

#connection.close();
