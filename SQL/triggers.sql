-- Trigger to decrease stock of book when order is placed
CREATE TRIGGER decrease_stock
  AFTER INSERT ON ORDER_CONTAINS
  BEGIN
    UPDATE BOOK SET stock = stock - NEW.quantity WHERE BOOK.ISBN = NEW.ISBN;
  END;

-- Trigger to add tracking and date info to new orders
CREATE TRIGGER order_time
  AFTER INSERT ON ORDER_TABLE
  BEGIN
    UPDATE ORDER_TABLE SET date_placed = DATETIME('NOW') WHERE ORDER_TABLE.onum = NEW.onum;
    UPDATE ORDER_TABLE SET tracking_num = abs(random()) WHERE ORDER_TABLE.onum = NEW.onum;
    UPDATE ORDER_TABLE SET est_arrival = DATETIME(date_placed, '+10 days') WHERE ORDER_TABLE.onum = NEW.onum;
  END;

-- Trigger to check if stock is less than 5, if it is "reorder" and add number of books equal to the amount purchased in the current month to the stock
CREATE TRIGGER reorder_check
  AFTER UPDATE ON BOOK WHEN New.stock < 5
  BEGIN
    UPDATE BOOK
    SET stock = stock + (SELECT SUM(ORDER_CONTAINS.quantity)
                         FROM ORDER_CONTAINS JOIN ORDER_TABLE ON ORDER_CONTAINS.onum = ORDER_TABLE.onum
                         WHERE ORDER_CONTAINS.ISBN = New.ISBN AND strftime('%Y-%m', date_placed) = strftime('%Y-%m', DATETIME('NOW')))
    WHERE BOOK.ISBN = NEW.ISBN;
  END;
