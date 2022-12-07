CREATE TABLE IF NOT EXISTS Publisher_Info(
  pid       INT PRIMARY KEY,
  name      VARCHAR(255),
  address   VARCHAR(255),
  email     VARCHAR(255),
  phone_num CHAR(10),
  bank_num  CHAR(10) NOT NULL
);

CREATE TABLE IF NOT EXISTS BOOK(
  ISBN      CHAR(13) PRIMARY KEY,
  title     VARCHAR(255) NOT NULL,
  year_pub  INT,
  num_pages INT,
  price     DECIMAL(10,2) NOT NULL,
  stock     INT NOT NULL,
  sales     INT NOT NULL,
  pid       INT NOT NULL,
  FOREIGN KEY(pid) REFERENCES Publisher_Info(pid),
  pub_cut   DECIMAl(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS GENRES(
  ISBN    CHAR(13),
  FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
  genre   VARCHAR(25),
  PRIMARY KEY(ISBN, genre)
);

CREATE TABLE IF NOT EXISTS AUTHORS(
  ISBN          CHAR(13),
  FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
  author_name   VARCHAR(255),
  PRIMARY KEY(ISBN, author_name)
);

CREATE TABLE IF NOT EXISTS CREDIT_CARD(
  cid         INT PRIMARY KEY,
  card_num    CHAR(10) NOT NULL,
  name        VARCHAR(255) NOT NULL,
  postal_code CHAR(6) NOT NULL
);

CREATE TABLE IF NOT EXISTS USER_TABLE(
  uid           INT PRIMARY KEY,
  email         VARCHAR(255) NOT NULL,
  password      VARCHAR(20) NOT NULL,
  address       VARCHAR(255),
  default_card  INT,
  FOREIGN KEY (default_card) REFERENCES CREDIT_CARD(cid),
  is_admin      BIT
);

CREATE TABLE IF NOT EXISTS ORDER_TABLE(
  onum            INT PRIMARY KEY,
  tracking_num    INT,
  uid             INT,
  FOREIGN KEY (uid) REFERENCES USER_TABLE(uid),
  payment         INT,
  FOREIGN KEY (payment) REFERENCES CREDIT_CARD(cid)
);

CREATE TABLE IF NOT EXISTS ORDER_CONTAINS(
  onum    INT,
  FOREIGN KEY (onum) REFERENCES ORDER_TABLE(onum),
  ISBN    CHAR(13),
  FOREIGN KEY (ISBN) REFERENCES BOOK(ISBN),
  PRIMARY KEY(onum, ISBN)
);
