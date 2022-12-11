-- Make Admin Account and Corresponding credit card
INSERT INTO USER_TABLE(username, email, password, is_admin) VALUES ('grbookworm1818', 'admin@thebookstore.com', 'password', 1);
INSERT INTO CREDIT_CARD(card_num, name, postal_code) VALUES (1234123412, 'Gertrude Robinson', 123123)

-- Insert two starting publishers (without contact info)
INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES('Harper-Collins', 1234567890);
INSERT INTO PUBLISHER_INFO(name, bank_num) VALUES('Penguin Random House', 1234512345);

-- Insert some books, publisher info is not accurate to real world
INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0571056865, 'Lord of the Flies', 1954, 224, 15.95, 15, 'Harper-Collins', 0.25);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0571056865, 'William Golding')
INSERT INTO GENRES(ISBN, genre) VALUES(0571056865, 'YA'),(0571056865, 'Allegorical')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0142424170, 'The Fault in Our Stars', 2012, 352, 19.95, 20, 'Harper-Collins', 0.45);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0142424170, 'John Green')
INSERT INTO GENRES(ISBN, genre) VALUES(0142424170, 'YA'),(0142424170, 'Romance')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0063071657, 'Heres To Us', 2021, 448, 24.95, 18, 'Harper-Collins', 0.85);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0063071657, 'Becky Albertalli'),(0063071657, 'Adam Silvera')
INSERT INTO GENRES(ISBN, genre) VALUES(0063071657, 'YA'),(0063071657, 'Romance'),(0063071657, 'LGBT')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0062457799, 'They Both Die At The End', 2018, 389, 9.95, 11, 'Penguin Random House', 0.75);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0062457799, 'Adam Silvera')
INSERT INTO GENRES(ISBN, genre) VALUES(0062457799, 'YA'),(0062457799, 'Romance'),(0062457799, 'LGBT')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0141439513, 'Pride and Prejudice', 1813, 279, 15.49, 6, 'Penguin Random House', 0.60);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0141439513, 'Jane Austen')
INSERT INTO GENRES(ISBN, genre) VALUES(0141439513, 'Classics'),(0141439513, 'Romance')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(9780486278, 'The Picture of Dorian Grey', 1891, 176, 6.49, 7, 'Penguin Random House', 0.64);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(9780486278, 'Oscar Wilde')
INSERT INTO GENRES(ISBN, genre) VALUES(9780486278, 'Classics'),(9780486278, 'Gothic')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(‎0553573403, 'Game of Thrones', 1997, 864, 13.59, 10, 'Penguin Random House', 0.50);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(‎0553573403, 'George R R Martin')
INSERT INTO GENRES(ISBN, genre) VALUES(‎0553573403, 'Fantasy'),(‎0553573403, 'Medieval')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(1524796280, 'Fire and Blood', 2018, 736, 47.00, 6, 'Penguin Random House', 0.35);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(‎1524796280, 'George R R Martin')
INSERT INTO GENRES(ISBN, genre) VALUES(‎1524796280, 'Fantasy'),(‎1524796280, 'Medieval'),(‎1524796280, 'History')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0441172717, 'Dune', 1990, 896, 11.58, 16, 'Harper-Collins', 0.52);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0441172717, 'Frank Herbert')
INSERT INTO GENRES(ISBN, genre) VALUES(0441172717, 'Fantasy'),(0441172717, 'Science Fiction')

INSERT INTO BOOK(ISBN, title, year_pub, num_pages, price, stock, pub_name, pub_cut) VALUES(0060853980, 'Good Omens: The Nice and Accurate Prophecies of Agnes Nutter, Witch', 2006, 512, 18.42, 8, 'Harper-Collins', 0.52);
INSERT INTO AUTHORS(ISBN, author_name) VALUES(0060853980, 'Neil Gaiman'), (0060853980, 'Terry Pratchett')
INSERT INTO GENRES(ISBN, genre) VALUES(0060853980, 'Fantasy'),(0060853980, 'Comedy')


-- INSERT older records to show that the reports work
INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2016-04-01 20:13:20')
INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(1, 0141439513, 5)

INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2016-04-12 20:13:20')
INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(2, 0062457799, 2)

INSERT INTO ORDER_TABLE(username, payment, delivery_address, date_placed) VALUES('grbookworm1818', 1, 'The Magnus Institute, London', '2018-03-18 20:13:20')
INSERT INTO ORDER_CONTAINS(onum, ISBN, quantity) VALUES(3, 0142424170, 2)
