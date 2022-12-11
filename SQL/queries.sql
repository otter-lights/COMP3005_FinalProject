-- SELECT Statement to Search for Books (?) used as placeholder for search term
SELECT ISBN, title, price FROM BOOK WHERE title=?;
SELECT ISBN, title, price FROM BOOK WHERE ISBN=?;
SELECT BOOK.ISBN, title, price FROM BOOK JOIN AUTHORS ON BOOK.ISBN=AUTHORS.ISBN WHERE author_name=?;
SELECT BOOK.ISBN, title, price FROM BOOK JOIN GENRES ON BOOK.ISBN=GENRES.ISBN WHERE genre=?;

-- Query to validate account password + Status
SELECT username, password, is_admin FROM USER_TABLE WHERE username="";

-- Create new credit card, cid will generate automatically as AUTOINCREMENT
INSERT INTO CREDIT_CARD(card_num, name, postal_code) VALUES (?, ?, ?);

-- Retrieve most recently added cid
SELECT MAX(cid) FROM CREDIT_CARD;

--Statements to create new account, depending on what info is given. 0 at end indicates a non-admin account
INSERT INTO USER_TABLE(username, email, password, address, default_card, is_admin) VALUES(?, ?, ?, ?, ?, 0);
INSERT INTO USER_TABLE(username, email, password, default_card, is_admin) VALUES(?, ?, ?, ?, 0);
INSERT INTO USER_TABLE(username, email, password, address, is_admin) VALUES(?, ?, ?, ?, 0);
INSERT INTO USER_TABLE(username, email, password, is_admin) VALUES(?, ?, ?, 0);

-- Add new publisher with and without contact information
INSERT INTO PUBLISHER_INFO(name, address, email, phone_num, bank_num) VALUES(?,?,?,?,?);
INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES(?,?);

-- Check if publisher exists based on a name
SELECT * FROM PUBLISHER_INFO WHERE name=?;

-- Add new book information
INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(?,?,?,?,?,?,?,?);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(?,?);
INSERT INTO GENRES(ISBN, genre) VALUES(?,?);

-- Place new order
INSERT INTO ORDER_TABLE(username, payment, delivery_address) VALUES(?,?,?);

-- Add books to order, repeated for each isbn
INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(?,?,?);

-- QUERIES TO SHOW REPORTS

-- Table of Year-Month | Num Books Purchased | Total Price | Total Profit
  SELECT strftime('%Y-%m', date_placed) year_month, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
  FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN
  GROUP BY year_month;

-- Table of Genre | Num Purchased | Total Price | Total Profit
  SELECT genre, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
  FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN JOIN GENRES ON BOOK.ISBN = GENRES.ISBN
  GROUP BY genre;

-- Table of Author Name | Num Purchased | Total Price | Total Profit
  SELECT author_name, SUM(quantity), SUM(price * quantity), SUM((price - (price * pub_cut)) * quantity)
  FROM ORDER_TABLE JOIN ORDER_CONTAINS ON ORDER_CONTAINS.onum = ORDER_TABLE.onum JOIN BOOK ON ORDER_CONTAINS.ISBN = BOOK.ISBN JOIN AUTHORS ON BOOK.ISBN = AUTHORS.ISBN
  GROUP BY author_name;
