#https://www.geeksforgeeks.org/sql-using-python/
import sqlite3
connection = sqlite3.connect('project.db');
connection.execute("PRAGMA foreign_keys = 1;");

# cursor
crsr = connection.cursor();
print("Connected to the database")
# SQL command to create a table in the database
createPubInfoTable = """CREATE TABLE IF NOT EXISTS PUBLISHER_INFO(
  pid       INTEGER PRIMARY KEY AUTOINCREMENT,
  name      VARCHAR(255),
  address   VARCHAR(255),
  email     VARCHAR(255),
  phone_num CHAR(10),
  bank_num  CHAR(10) NOT NULL
);"""
## execute the statement
crsr.execute(createPubInfoTable);

createBookTable = """CREATE TABLE IF NOT EXISTS BOOK(
  ISBN      CHAR(13) PRIMARY KEY,
  title     VARCHAR(255) NOT NULL,
  year_pub  INT,
  num_pages INT,
  price     DECIMAL(10,2) NOT NULL,
  stock     INT NOT NULL,
  sales     INT NOT NULL,
  pid       INT NOT NULL,
  pub_cut   DECIMAl(10,2) NOT NULL,
  FOREIGN KEY(pid)
    REFERENCES Publisher_Info(pid)
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
  uid           INTEGER PRIMARY KEY AUTOINCREMENT,
  email         VARCHAR(255) NOT NULL UNIQUE,
  password      VARCHAR(20) NOT NULL,
  address       VARCHAR(255),
  default_card  INT,
  is_admin      BIT,
  FOREIGN KEY (default_card)
    REFERENCES CREDIT_CARD(cid)
);"""
crsr.execute(createUserTable);

createOrderTable = """CREATE TABLE IF NOT EXISTS ORDER_TABLE(
  onum            INTEGER PRIMARY KEY AUTOINCREMENT,
  tracking_num    INT,
  uid             INT,
  payment         INT,
  FOREIGN KEY (payment)
    REFERENCES CREDIT_CARD(cid),
  FOREIGN KEY (uid)
    REFERENCES USER_TABLE(uid)
);"""
crsr.execute(createOrderTable);

createContainsTable = """CREATE TABLE IF NOT EXISTS ORDER_CONTAINS(
  onum    INT,
  ISBN    CHAR(13),
  PRIMARY KEY(onum, ISBN),
  FOREIGN KEY (ISBN)
    REFERENCES BOOK(ISBN),
  FOREIGN KEY (onum)
    REFERENCES ORDER_TABLE(onum)
);"""
crsr.execute(createContainsTable);

admin_account = """INSERT INTO USER_TABLE(email, password, is_admin) VALUES ('admin@thebookstore.com', 'grbookworm1818', 1);"""
crsr.execute(admin_account);
connection.commit();
# close the connection
connection.close();
