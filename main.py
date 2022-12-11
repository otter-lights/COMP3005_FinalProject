import sqlite3
connection = sqlite3.connect('project.db');
connection.execute("PRAGMA foreign_keys = 1;");
crsr = connection.cursor();

logged_in = False
is_admin = False
cart = []
cartq = {}

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

        if(logged_in != False and is_admin == False):
            add = input(f"Would you like to add {info[1]} to cart? (y/n) ")
            if(add == "y" or add == "Y"):
                if(info[0] not in cartq):
                    cartq[info[0]] = 1
                    cart.append([info[0], info[1], info[4], 1]);
                else:
                    cartq[info[0]] += 1
                print("Added to Cart", info[0])
        elif(logged_in != False and is_admin == True):
            delete = input(f"Would you like to delete {info[1]} from store? (y/n) ")
            if(delete == "y" or delete == "Y"):
                crsr.execute("DELETE FROM AUTHORS WHERE ISBN=?;", (info[0],))
                crsr.execute("DELETE FROM GENRES WHERE ISBN=?;", (info[0],))
                crsr.execute("DELETE FROM BOOK WHERE ISBN=?;", (info[0],))

                connection.commit()
        else:
            print("Add to Cart Not Available (Not Logged In). Returning to Search Menu...")
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
    username = input("Username: ")
    password = input("Password: ")
    crsr.execute("SELECT username, password, is_admin FROM USER_TABLE WHERE username=?", (username,))
    ans = crsr.fetchone()
    if(not ans):
        print("No account exists with that username.\nReturning to menu...")
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
    while(True):
        username = input("Username: ")
        crsr.execute("SELECT * FROM USER_TABLE WHERE username=?;", (username,))
        if(crsr.fetchone()):
            print("Username already in use. Choose a different name.")
        else:
            break
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
            crsr.execute('INSERT INTO USER_TABLE(username, email, password, address, default_card, is_admin) VALUES(?, ?, ?, ?, ?, 0);', (username, email, password, address, new_cid,))
        else:
            crsr.execute('INSERT INTO USER_TABLE(username, email, password, default_card, is_admin) VALUES(?, ?, ?, ?, 0);', (username, email, password, new_cid,))
    else:
        address = input("Would you like to set a default address? (y/n)")
        if(address == "y" or address == "Y"):
            address = input("Address: ")
            print("test")
            crsr.execute('INSERT INTO USER_TABLE(username, email, password, address, is_admin) VALUES(?, ?, ?, ?, 0);', (username, email, password, address,))
        else:
            crsr.execute('INSERT INTO USER_TABLE(username, email, password, is_admin) VALUES(?, ?, ?, 0);', (username, email, password,))

    connection.commit()
    print("Creating Account...")
    return(username)

def addPublisher(pub_name):
    bank_num = input(" Bank Number (10 Digits): ")
    if(len(bank_num) != 10):
        print("Incorrect Input. Returning to Menu...")
        return("error")
    contact = input(" Would you like to add contact information? (y/n) ")
    if(contact == "y" or contact == "Y"):
        address = input(" Address: ")
        email = input(" Email: ")
        phone_num = input(" Phone Number (10 Digits): ")
        if(len(phone_num) != 10):
            print("Incorrect Input. Returning to Menu...")
            return("error")
        crsr.execute('INSERT INTO PUBLISHER_INFO(name, address, email, phone_num, bank_num) VALUES(?,?,?,?,?);', (pub_name, address, email, phone_num, bank_num,))
    else:
        crsr.execute('INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES(?,?);', (pub_name, bank_num,))

    connection.commit()
    print("Creating Publisher Info...")
    return(pub_name)

def addbooks():
    while(True):
        isbn = input(" ISBN: ")
        title = input(" Title: ")
        year_pub = input(" Year Published: ")
        num_pages = input(" Num Pages: ")
        price = input(" Price: ")
        stock = input(" Staring Stock: ")

        pub_name = input(" Publisher Name: ")
        crsr.execute("SELECT * FROM PUBLISHER_INFO WHERE name=?", (pub_name,))
        options = crsr.fetchone()
        if(options):
            print("Returned Publisher Information: ", options)
            test = input("Is this correct? (y/n) ")
            if(test == "y" or test == "Y"):
                pname = options[0][0]
            else:
                print("Returning to Menu...")
                break
        else:
            new = input("No Match. Would you like to make a new publisher record under this name? (y/n) ")
            if(new == "y" or new == "Y"):
                pname = addPublisher(pub_name)
                if(pname == "error"):
                    print("Returning to Menu...")
                    break
            else:
                print("Returning to Menu...")
                break


        pub_cut = input(" Publisher Percent Cut: ")
        print(" Prompt for author name will repeat (for multiple authors) until 'q' is submitted to end." )
        authors = []
        while(True):
            author = input(" Author Name: ")
            if(author == "q" or author == "Q"):
                break
            authors.append(author)

        print(" Genre tag prompt will repeat (until 'q'), write one on each line." )
        genres = []
        while(True):
            genre = input(" Genre: ")
            if(genre == "q" or genre == "Q"):
                break
            genres.append(genre)

        crsr.execute("INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(?,?,?,?,?,?,?,?);", (isbn, title, year_pub, num_pages, price, stock, pname, pub_cut))
        for i in range(len(authors)):
            crsr.execute("INSERT INTO AUTHORS(ISBN, author_name) VALUES(?,?);", (isbn, authors[i],))
        for i in range(len(genres)):
            crsr.execute("INSERT INTO GENRES(ISBN, genre) VALUES(?,?);", (isbn, genres[i],))

        connection.commit()

        end = input("Would you like to add another book? (y/n) ")
        if(end == "n" or end == "N"):
            break

def checkout(total):
    daddress = input("Would you like to use your default address? (y/n) ")
    if(daddress == "y" or daddress == "Y"):
        crsr.execute("SELECT address FROM USER_TABLE WHERE username=?;", (logged_in,))
        address = crsr.fetchone()[0]
        if(address == None):
            print("No Default Address Set.")
            makeaddress = input("Would you like to input a new address? (y/n) ")
            if(makeaddress == "y" or makeaddress == "Y"):
                address = input("Address: ")
            else:
                print("Error with Address. Returning to Menu...")
                return()
    else:
        makeaddress = input("Would you like to input a new address? (y/n) ")
        if(makeaddress == "y" or makeaddress == "Y"):
            address = input("Address: ")
        else:
            print("Error with Address. Returning to Menu...")
            return()
    default = input("Would you like to use your default card to check out? (y/n) ")
    if(default == "y" or default == "Y"):
        crsr.execute("SELECT default_card FROM USER_TABLE WHERE username=?;", (logged_in,))
        payment = crsr.fetchone()[0]
        if(payment == None):
            print("No Default Card Set.")
            makecard = input("Would you like to input a new card? (y/n) ")
            if(makecard == "y" or makecard == "Y"):
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
                payment = crsr.execute('SELECT MAX(cid) FROM CREDIT_CARD').fetchone()[0] #MAX(cid) will get the most recent since we are using autoincrement
            else:
                print("Error with Payment. Returning to Menu...")
                return()
    else:
        makecard = input("Would you like to input a new card? (y/n) ")
        if(makecard == "y" or makecard == "Y"):
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
            payment = crsr.execute('SELECT MAX(cid) FROM CREDIT_CARD').fetchone()[0] #MAX(cid) will get the most recent since we are using autoincrement
        else:
            print("Error with Payment. Returning to Menu...")
            return()

    crsr.execute("INSERT INTO ORDER_TABLE(username, payment, delivery_address) VALUES(?,?,?);", (logged_in, payment, address, ))
    new_onum = crsr.execute('SELECT MAX(onum) FROM ORDER_TABLE').fetchone()[0]

    for i in range(len(cart)):
        crsr.execute("INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(?,?,?);", (new_onum, cart[i][0], cartq[cart[i][0]]))

    connection.commit()
    cart.clear()
    cartq.clear()
    print("Checking Out...")
    print("Order Number:", new_onum)


def viewcart():
    if(cart):
        total = 0
        for i in range(len(cart)):
            print(i+1, cart[i][1], cart[i][2], "(x", cartq[cart[i][0]], ")")
            total += cart[i][2] * cartq[cart[i][0]]
        print("-----\nTotal: ", total)
        remove = input("Would you like to remove a book? (y/n)")
        if(remove == "y" or remove == "Y"):
            remove = input("Type number corresponding to book to remove from cart: ")
            if(remove.isdigit() and int(remove) <= len(remove)+1):
                if(cartq[cart[int(remove)-1][0]] == 1):
                    cartq.pop(cart[int(remove)-1][0])
                    cart.pop(int(remove)-1)
                else:
                    cartq[cart[int(remove)-1][0]] -= 1
                viewcart()
                return()
            else:
                print("Choice not understood...")
                viewcart()
                return()
        cout = input("Would you like to check out now? (y/n) ")
        if(cout == "y" or cout == "Y"):
            checkout(total)
        else:
            print("Returning to Menu...")
    else:
        print("Cart is Empty. Returning to Menu ...")
        return()

def viewreports():
    report = input(" (1) Income vs Profit, per Month \n (2) Income vs Profit, per Author \n (3) Income vs Profit, per Genre \n")
    if(report == "1"):
        crsr.execute("""
            SELECT strftime('%Y-%m', date_placed) year_month, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
            FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN
            GROUP BY year_month;
        """)
        print("Year-Month | Num Sales | Income | Profit")
        for row in crsr.fetchall():
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
    elif(report == "2"):
        crsr.execute("""
            SELECT author_name, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
            FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN JOIN AUTHORS ON BOOK.ISBN = AUTHORS.ISBN
            GROUP BY author_name;
        """)
        print("Author | Num Sales | Income | Profit")
        for row in crsr.fetchall():
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
    elif(report == "3"):
        crsr.execute("""
            SELECT genre, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
            FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN JOIN GENRES ON BOOK.ISBN = GENRES.ISBN
            GROUP BY genre;
        """)
        print("Genre | Num Sales | Income | Profit")
        for row in crsr.fetchall():
            print(row[0], "|", row[1], "|", row[2], "|", row[3])
    else:
        print("Input Not Recognized. Returning to Menu...")

def trackorder():
    onum = input("Type Order Number to View Tracking ID: ")
    crsr.execute("SELECT tracking_num, est_arrival, delivery_address FROM ORDER_TABLE WHERE onum=? AND username=?;", (onum,logged_in,))
    tracking_info = crsr.fetchone()
    if(tracking_info):
        print("Tracking Number:", tracking_info[0]);
        print("Estimated Arrival:", tracking_info[1]);
        print("Delivery Address:", tracking_info[2])
    else:
        print("Provided order number not valid")
    another = input("Would you like to track another order? (y/n) ")
    if(another == "y" or another == "Y"):
        trackorder()

while(True):
    if(logged_in != False and is_admin == False):
        print("\nWelcome to TheBookStore.", logged_in, "\nPlease choose an option from the following menu: ")
        option = input(" (1) Browse Our Collection \n (2) View Cart \n (3) Track Order \n (4) Exit Store \n")
        if(option == "1"):
            browse()
        elif(option == "2"):
            viewcart()
        elif(option == "3"):
            trackorder()
        elif(option == "4"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;
    elif(logged_in != False and is_admin == True):
        print("\nWelcome to TheBookStore [ADMIN VIEW].", logged_in, "\nPlease choose an option from the following menu: ")
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
        print("\nWelcome to TheBookStore. \nPlease choose an option from the following menu: ")
        option = input(" (1) Browse Our Collection \n (2) Log In \n (3) Create a New Account \n (4) Exit Store \n")
        #print(option)
        if(option == "1"):
            browse()
        elif(option == "2"):
            logged_in, is_admin = login()
        elif(option == "3"):
            logged_in = createaccount()
        elif(option == "4"):
            print("Exiting Program ...")
            break;
        else:
            print("Sorry, we didn't understand that input. Please choose from the options below: ")
            continue;

connection.close();
