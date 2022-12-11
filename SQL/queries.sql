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

-- Table of Book Name | Price | Profit for Store
SELECT title, price, price - (price * pub_cut)
FROM BOOK;
