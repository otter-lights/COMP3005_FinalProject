CREATE TABLE IF NOT EXISTS Publisher_Info(
  pid       INT PRIMARY KEY,
  name      VARCHAR(255),
  address   VARCHAR(255),
  email     VARCHAR(255),
  phone_num CHAR(10),
  bank_num  CHAR(10)
);

CREATE TABLE IF NOT EXISTS BOOK(
  ISBN      CHAR(13) PRIMARY KEY,
  title     VARCHAR(255) NOT NULL,
  year_pub  INT,
  num_pages INT,
  price     DECIMAL(10,2) NOT NULL,
  stock     INT NOT NULL,
  sales     INT NOT NULL,
  pid       INT,
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

/*

CREATE TABLE IF NOT EXISTS Department(
  dname           VARCHAR(15) UNIQUE NOT NULL,
  dnumber         INT PRIMARY KEY,
  mgr_ssn         CHAR(9),
  FOREIGN KEY (mgr_ssn) REFERENCES Employee(ssn),
  mgr_start_date  DATE
);

ALTER TABLE Employee
  ADD FOREIGN KEY(dno) REFERENCES Department(dnumber);

CREATE TABLE IF NOT EXISTS DEPT_LOCATIONS(
  dnumber   INT,
  FOREIGN KEY(dnumber) REFERENCES Department(dnumber),
  dlocation VARCHAR(15),
  PRIMARY KEY(dnumber, dlocation)
);

CREATE TABLE IF NOT EXISTS PROJECT(
  pname       VARCHAR(15) UNIQUE NOT NULL,
  pnumber     INT PRIMARY KEY,
  plocation   VARCHAR(15),
  dnum        INT NOT NULL,
  FOREIGN KEY(dnum) REFERENCES Department(dnumber)
);

CREATE TABLE IF NOT EXISTS WORKS_ON(
  essn  CHAR(9),
  FOREIGN KEY (essn) REFERENCES Employee(ssn),
  pno   INT,
  FOREIGN KEY (pno) REFERENCES PROJECT(pnumber),
  hours   NUMERIC(3,1) NOT NULL,
  PRIMARY KEY(essn, pno)
);

CREATE TABLE IF NOT EXISTS DEPENDENT(
  essn            CHAR(9),
  FOREIGN KEY (essn) REFERENCES Employee(ssn),
  dependent_name  VARCHAR(15),
  sex             CHAR(1),
  bdate           DATE,
  relationship    VARCHAR(8),
  PRIMARY KEY(essn, dependent_name)
);
