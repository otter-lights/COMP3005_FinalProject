import sqlite3
connection = sqlite3.connect('project.db');
connection.execute("PRAGMA foreign_keys = 1;");
crsr = connection.cursor();


logged_in = False
is_admin = False

def selection(results):
    for i in range(1, len(results)+1):
        book = results[i-1]
        isbn = book[0]
        print(i, book[1], book[2])
    selection = input("Enter number of book to select: ")
    if(selection.isdigit() and int(selection) < len(results)+1):
        choice = results[int(selection)-1]
        isbn = choice[0]
        crsr.execute("SELECT * FROM BOOK WHERE isbn=?", (isbn,))
        info = crsr.fetchone()
        crsr.execute("SELECT author_name FROM AUTHORS WHERE isbn=?", (isbn,))
        authors = crsr.fetchall()
        author_str = " Authors: "
        for i in range(len(authors)):
            if(i == len(authors)-1):
                author_str += str(authors[i][0])
            else:
                author_str += str(authors[i][0]) + " & "

        crsr.execute("SELECT genre FROM GENRES WHERE isbn=?", (isbn,))
        genres = crsr.fetchall()
        genre_str = " Genres: "
        for i in range(len(genres)):
            if(i == len(genres)-1):
                genre_str += str(genres[i][0])
            else:
                genre_str += str(genres[i][0]) + ", "

        print(" Title: ", info[1])
        print(author_str)
        print(genre_str)
        print(" Price: ", info[4])
        print(" ISBN: ", info[0])
        print(" Year Published: ", info[2])
        print(" Number of Pages: ", info[3])
        if(info[5] > 0):
            print(" Status: In Stock")
        else:
            print(" Status: Out of Stock")

        #GIVE OPTIONS
        print("\n")
    else:
        print("input not understood, ending search")

def browse():
    while(True):
        search_type = input("Would you like to search by: \n (1) title \n (2) ISBN \n (3) author name \n (4) genre \n ")
        if(search_type == "1"):
            title = input("Title: ")
            crsr.execute("SELECT ISBN, title, price FROM BOOK WHERE title=?", (title,))
            selection(crsr.fetchall())
        elif(search_type == "2"):
            while(True):
                isbn = input("ISBN (10 Digits): ")
                if(len(isbn) != 10):
                    print("incorrect length, try again")
                    continue
                break
            crsr.execute("SELECT ISBN, title, price FROM BOOK WHERE ISBN=?", (int(isbn),))
            #crsr.execute("SELECT ISBN, title, year_pub, price FROM BOOK WHERE ISBN=0062457799")
            selection(crsr.fetchall())
        elif(search_type == "3"):
            name = input("Author Name: ")
            crsr.execute("SELECT BOOK.ISBN, title, price FROM BOOK JOIN AUTHORS ON BOOK.ISBN=AUTHORS.ISBN WHERE author_name=?", (name,))
            selection(crsr.fetchall())
        elif(search_type == "4"):
            genre = input("Genre: ")
            crsr.execute("SELECT BOOK.ISBN, title, price FROM BOOK JOIN GENRES ON BOOK.ISBN=GENRES.ISBN WHERE genre=?", (genre,))
            selection(crsr.fetchall())
            #print(results)
        else:
            print("input was not understood, please try again")
            continue
        end = input(" (1) Return To Menu \n (2) New Search \n ") #POTENTIALLY ADD OPTION TO REDO LAST SEARCH
        if(end == "1"):
            print("Returning To Menu ...")
            break
        elif(end == "2"):
            continue
        else:
            print("input was not understood, returning to menu")
            break

def login():
    email = input("Email: ")
    password = input("Password: ")
    crsr.execute("SELECT uid, password, is_admin FROM USER_TABLE WHERE email=?", (email,))
    ans = crsr.fetchone()
    print(ans)
    if(not ans):
        print("No account exists with that email.\nReturning to menu...")
        return(False, False)
    elif(ans[1] == password):
        print("Logging In...")
        if(ans[2] == 1):
            return(ans[0], True)
        else:
            return(ans[0], False)
    else:
        print("Incorrect password. \nReturning to menu...")
        return(False, False)

def createaccount():
    email = input("Email: ")
    password = input("Password: ")
    card = input("Would you like to set a default card? (y/n)? ")
    if(card == "y" or card == "Y"):
        while(True):
            c = input("Card Number (10 Characters): ")
            if(len(c) == 10):
                break
        n = input("Name on Card: ")
        while(True):
            pc = input("Postal Code for Card (6 Characters): ")
            if(len(pc) == 6):
                break

        crsr.execute('INSERT INTO CREDIT_CARD(card_num, name, postal_code) VALUES (?, ?, ?);', (c, n, pc,))
        new_cid = crsr.execute('SELECT MAX(cid) FROM CREDIT_CARD').fetchone()[0] #MAX(cid) will get the most recent since we are using autoincrement

        address = input("Would you like to set a default address? (y/n)")
        if(address == "y" or address == "Y"):
            address = input("Address: ")
            crsr.execute('INSERT INTO USER_TABLE(email, password, address, default_card, is_admin) VALUES(?, ?, ?, ?, 0);', (email, password, address, new_cid,))
        else:
            crsr.execute('INSERT INTO USER_TABLE(email, password, default_card, is_admin) VALUES(?, ?, ?, 0);', (email, password, new_cid,))
    else:
        address = input("Would you like to set a default address? (y/n)")
        if(address == "y" or address == "Y"):
            address = input("Address: ")
            print("test")
            crsr.execute('INSERT INTO USER_TABLE(email, password, address, is_admin) VALUES(?, ?, ?, 0);', (email, password, address,))
        else:
            crsr.execute('INSERT INTO USER_TABLE(email, password, is_admin) VALUES(?, ?, 0);', (email, password,))

    connection.commit()
    new_user = crsr.execute('SELECT MAX(uid) FROM USER_TABLE').fetchone()[0]
    print("Creating Account...")
    return(new_user)

def addbooks():
    while(True):
        #ask ISBN
        #ask title
        #ask year_pub and num_pages (optional)
        #ask author(s)
        #ask genre(s)
        #ask price
        #ask stock
        #ask publisher name (and look up), if not exist make new PUBLISHER_INFO
        #ask pub_cut

        end = input("Would you like to add another book? (y/n) ")
        if(end == "n" or end == "N"):
            break

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
        option = input(" (1) Browse Our Collection \n (2) View Reports \n (3) Add Books \n (4) Exit Store \n")
        if(option == "1"):
            browse()
        elif(option == "2"):
            viewreports()
        elif(option == "3"):
            addbooks()
        elif(option == "4"):
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
            logged_in = createaccount()
        elif(option == "5"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;

connection.close();
