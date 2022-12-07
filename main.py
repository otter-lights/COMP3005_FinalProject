#https://www.geeksforgeeks.org/sql-using-python/
import sqlite3
connection = sqlite3.connect('gfg.db')

# cursor
crsr = connection.cursor()
 
# SQL command to create a table in the database
sql_command = """CREATE TABLE IF NOT EXISTS Publisher_Info(
  pid       INT PRIMARY KEY,
  name      VARCHAR(255),
  address   VARCHAR(255),
  email     VARCHAR(255),
  phone_num CHAR(10),
  bank_num  CHAR(10) NOT NULL
);"""
 
# execute the statement
crsr.execute(sql_command)
 
# close the connection
connection.close()
