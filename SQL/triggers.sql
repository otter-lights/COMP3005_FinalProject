CREATE TRIGGER order_more_book
   AFTER INSERT ON ORDER_CONTAINS
BEGIN
   SELECT
      CASE
	WHEN NEW.email NOT LIKE '%_@__%.__%' THEN
   	  RAISE (ABORT,'Invalid email address')
       END;
END;
