#https://www.geeksforgeeks.org/sql-using-python/
import sqlite3
connection = sqlite3.connect('project.db');
connection.execute("PRAGMA foreign_keys = 1;");
stock_trigger = 2;

# cursor
crsr = connection.cursor();
print("Connected to the database")
# SQL command to create a table in the database
createPubInfoTable = """CREATE TABLE IF NOT EXISTS PUBLISHER_INFO(
  name      VARCHAR(255) PRIMARY KEY,
  address   VARCHAR(255),
  email     VARCHAR(255),
  phone_num CHAR(10),
  bank_num  CHAR(10) NOT NULL
);"""
## execute the statement
crsr.execute(createPubInfoTable);

createBookTable = """CREATE TABLE IF NOT EXISTS BOOK(
  ISBN      CHAR(10) PRIMARY KEY,
  title     VARCHAR(255) NOT NULL,
  year_pub  INT NOT NULL,
  num_pages INT NOT NULL,
  price     DECIMAL(10,2) NOT NULL,
  stock     INT NOT NULL,
  pub_name  VARCHAR(255) NOT NULL,
  pub_cut   DECIMAl(10,2) NOT NULL,
  FOREIGN KEY(pub_name)
    REFERENCES Publisher_Info(name)
    ON DELETE CASCADE
);"""
crsr.execute(createBookTable);

createGenreTable = """CREATE TABLE IF NOT EXISTS GENRES(
  ISBN    CHAR(13),
  genre   VARCHAR(25),
  PRIMARY KEY(ISBN, genre),
  FOREIGN KEY (ISBN)
    REFERENCES BOOK(ISBN)
);"""
crsr.execute(createGenreTable);

createAuthorTable = """CREATE TABLE IF NOT EXISTS AUTHORS(
  ISBN          CHAR(13),
  author_name   VARCHAR(255),
  PRIMARY KEY(ISBN, author_name),
  FOREIGN KEY (ISBN)
    REFERENCES BOOK(ISBN)
);"""
crsr.execute(createAuthorTable);

createCCTable = """CREATE TABLE IF NOT EXISTS CREDIT_CARD(
  cid         INTEGER PRIMARY KEY AUTOINCREMENT,
  card_num    CHAR(10) NOT NULL,
  name        VARCHAR(255) NOT NULL,
  postal_code CHAR(6) NOT NULL
);"""
crsr.execute(createCCTable);

createUserTable = """CREATE TABLE IF NOT EXISTS USER_TABLE(
  username      VARCHAR(50) PRIMARY KEY,
  email         VARCHAR(255) NOT NULL,
  password      VARCHAR(20) NOT NULL,
  address       VARCHAR(255),
  default_card  INT,
  is_admin      BIT,
  FOREIGN KEY (default_card)
    REFERENCES CREDIT_CARD(cid)
);"""
crsr.execute(createUserTable);

createOrderTable = """CREATE TABLE IF NOT EXISTS ORDER_TABLE(
  onum                INTEGER PRIMARY KEY AUTOINCREMENT,
  tracking_num        INT,
  username            VARCHAR(50) NOT NULL,
  payment             INT NOT NULL,
  delivery_address    VARCHAR(255) NOT NULL,
  date_placed         TEXT,
  est_arrival         TEXT,
  FOREIGN KEY (payment)
    REFERENCES CREDIT_CARD(cid),
  FOREIGN KEY (username)
    REFERENCES USER_TABLE(username)
);"""
crsr.execute(createOrderTable);

createContainsTable = """CREATE TABLE IF NOT EXISTS ORDER_CONTAINS(
  onum     INT,
  ISBN     CHAR(13),
  quantity INT,
  PRIMARY KEY(onum, ISBN),
  FOREIGN KEY (ISBN)
    REFERENCES BOOK(ISBN),
  FOREIGN KEY (onum)
    REFERENCES ORDER_TABLE(onum)
);"""
crsr.execute(createContainsTable);

crsr.execute("""INSERT INTO USER_TABLE(username, email, password, is_admin) VALUES ('grbookworm1818', 'admin@thebookstore.com', 'password', 1);""");
crsr.execute("INSERT INTO CREDIT_CARD(card_num, name, postal_code) VALUES (1234123412, 'Gertrude Robinson', 123123)")

crsr.execute("""INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES('Harper-Collins', 1234567890);""")
crsr.execute("""INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES('Penguin Random House', 1234512345);""")

crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 15.95, 15, 'Harper-Collins', 0.25);""")
crsr.execute("""INSERT INTO AUTHORS(ISBN, author_name) VALUES(0571056865, 'William Golding')""")
crsr.execute("""INSERT INTO GENRES(ISBN, genre) VALUES(0571056865, 'YA'),(0571056865, 'Allegorical')""")

crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0142424170, 'The Fault in Our Stars', 2012, 352, 19.95, 20, 'Harper-Collins', 0.45);""")
crsr.execute("""INSERT INTO AUTHORS(ISBN, author_name) VALUES(0142424170, 'John Green')""")
crsr.execute("""INSERT INTO GENRES(ISBN, genre) VALUES(0142424170, 'YA'),(0142424170, 'Romance')""")

crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0063071657, 'Heres To Us', 2021, 448, 24.95, 18, 'Harper-Collins', 0.85);""")
crsr.execute("""INSERT INTO AUTHORS(ISBN, author_name) VALUES(0063071657, 'Becky Albertalli'),(0063071657, 'Adam Silvera')""")
crsr.execute("""INSERT INTO GENRES(ISBN, genre) VALUES(0063071657, 'YA'),(0063071657, 'Romance'),(0063071657, 'LGBT')""")

crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0062457799, 'They Both Die At The End', 2018, 389, 9.95, 11, 'Penguin Random House', 0.75);""")
crsr.execute("""INSERT INTO AUTHORS(ISBN, author_name) VALUES(0062457799, 'Adam Silvera')""")
crsr.execute("""INSERT INTO GENRES(ISBN, genre) VALUES(0062457799, 'YA'),(0062457799, 'Romance'),(0062457799, 'LGBT')""")

crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0141439513, 'Pride and Prejudice', 1813, 279, 15.49, 6, 'Penguin Random House', 0.60);""")
crsr.execute("""INSERT INTO AUTHORS(ISBN, author_name) VALUES(0141439513, 'Jane Austen')""")
crsr.execute("""INSERT INTO GENRES(ISBN, genre) VALUES(0141439513, 'Classics'),(0141439513, 'Romance')""")

#crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pid, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 30.49, 12, ?, 0.12);""", (example_pid2,))
#crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pid, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 35.95, 8, ?, 0.40);""", (example_pid1,))
#crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pid, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 18.95, 17, ?, 0.18);""", (example_pid2,))
#crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pid, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 8.25, 23, ?, 0.07);""", (example_pid2,))
#crsr.execute("""INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pid, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 15.25, 19, ?, 0.11);""", (example_pid1,))

crsr.execute("INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2016-04-01 20:13:20')")
crsr.execute("INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(1, 0141439513, 5)")

crsr.execute("INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2016-04-12 20:13:20')")
crsr.execute("INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(2, 0062457799, 2)")

crsr.execute("INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2018-03-18 20:13:20')")
crsr.execute("INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(3, 0142424170, 2)")

crsr.execute("""
CREATE TRIGGER decrease_stock
  AFTER INSERT ON ORDER_CONTAINS
  BEGIN
    UPDATE BOOK SET stock = stock - NEW.quantity WHERE BOOK.ISBN = NEW.ISBN;
  END;
""")

crsr.execute("""
CREATE TRIGGER order_time
  AFTER INSERT ON ORDER_TABLE
  BEGIN
    UPDATE ORDER_TABLE SET date_placed = DATETIME('NOW') WHERE ORDER_TABLE.onum = NEW.onum;
    UPDATE ORDER_TABLE SET tracking_num = abs(random()) WHERE ORDER_TABLE.onum = NEW.onum;
    UPDATE ORDER_TABLE SET est_arrival = DATETIME(date_placed, '+10 days') WHERE ORDER_TABLE.onum = NEW.onum;
  END;
""")

crsr.execute("""
CREATE TRIGGER reorder_check
  AFTER UPDATE ON BOOK WHEN New.stock < 5
  BEGIN
    UPDATE BOOK
    SET stock = (SELECT SUM(ORDER_CONTAINS.quantity)
                 FROM ORDER_CONTAINS JOIN ORDER_TABLE ON ORDER_CONTAINS.onum = ORDER_TABLE.onum
                 WHERE ORDER_CONTAINS.ISBN = New.ISBN AND strftime('%Y-%m', date_placed) = strftime('%Y-%m', DATETIME('NOW')))
    WHERE BOOK.ISBN = NEW.ISBN;
  END;
""")

connection.commit();
# close the connection
connection.close();
