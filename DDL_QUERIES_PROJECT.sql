--CREATE DATABASE PROJECT;
--DROP DATABASE PROJECT;
-------------------------------------------------------------------------------
CREATE TABLE CUSTOMER
(CustomerID VARCHAR(50),
CustomerName VARCHAR(50),
CustomerCity VARCHAR(50),
CustomerPhone VARCHAR(12),
CONSTRAINT CUSTOMER_PK PRIMARY KEY(CustomerID));

-----------------------------------------------------------------------------------
CREATE TABLE PRODUCT
(ProductID VARCHAR(50),
ProductName VARCHAR(50),
ProductPrice INT,
ProductQuantity INT,
CONSTRAINT PRODUCT_PK PRIMARY KEY(ProductID),
CONSTRAINT PRICE_CHECK CHECK (ProductPrice>=1),
CONSTRAINT Product_quan CHECK(ProductQuantity >=1));

INSERT INTO PRODUCT(ProductID,ProductName,ProductPrice,ProductQuantity)
VALUES('RI','RICE',240,20),('CO','COOKING OIL',520,20),('CD','COLD DRINK', 120,25),('BR','BREAD',100,25),
('FC','FRUIT CAKE',100,25),('FL','FLOUR',2000,30),('EG','EGG',120,25),('SU','SUGAR',220,25);
SELECT * FROM PRODUCT;

----------------------------------------------------------------------------------
CREATE TABLE SEARCHPRODUCT
(CustomerID VARCHAR(50),
ProductID VARCHAR(50),
CONSTRAINT SEARCH_PK PRIMARY KEY(CustomerID,ProductID),
CONSTRAINT SEARCH_FK1 FOREIGN KEY(CustomerID) REFERENCES CUSTOMER(CustomerID),
CONSTRAINT SEARCH_FK2 FOREIGN KEY(ProductID) REFERENCES PRODUCT (ProductID));
----------------------------------------------------------------------------------
CREATE TABLE ORDERR
(OrderID VARCHAR(50),
ProductID VARCHAR(50),
OrderDate VARCHAR(50), 
CONSTRAINT ORDERR_PK PRIMARY KEY(OrderID,ProductID),
CONSTRAINT ORDERR_FK1 FOREIGN KEY(ProductID) REFERENCES PRODUCT(ProductID));
-------------------------------------------------------------------------------
CREATE TABLE MANAGER
(ManagerID VARCHAR(50),
ManagerName VARCHAR(50),
CONSTRAINT MANAGER_PK PRIMARY KEY(ManagerID));

INSERT INTO MANAGER 
VALUES(1,'ALI'),(2,'AHMED'),(3,'AWAIS');

SELECT * FROM MANAGER;
--------------------------------------------------------------------------------
CREATE TABLE CASHIER
(CashierID VARCHAR(50),
CashierName VARCHAR(50),
CONSTRAINT Cashier_PK PRIMARY KEY(CashierID));

INSERT INTO CASHIER
VALUES(1,'AHMED'),(2,'ABDULLAH'),(3,'AHSAN');

SELECT * FROM CASHIER;
-----------------------------------------------------------------------------------
CREATE TABLE CHECKPAYMENT
(CheckID varchar(50),
BankID VARCHAR(50),
CustomerId VARCHAR(50),
TotalAmount VARCHAR(50),
CONSTRAINT CHECK_PK PRIMARY KEY(CheckID),
CONSTRAINT C_ID_FK FOREIGN KEY (CustomerId) REFERENCES CUSTOMER(CustomerID)) ;
---------------------------------------------------------------------------------
CREATE TABLE CASHPAYMENT
(CASHID varchar(50),
CustomerId VARCHAR(50),
TotalAmount VARCHAR(50),
CONSTRAINT CASH_PK PRIMARY KEY(CASHID),
CONSTRAINT CASH_FK1 FOREIGN KEY (CustomerId) REFERENCES CUSTOMER(CustomerID)) ;
---------------------------------------------------------------------------------
CREATE TABLE CREDITCARD
(CARDID varchar(50),
EXPIRYDATE DATE,
CREDIT_TYPE VARCHAR(50),
TotalAmount VARCHAR(50),
CustomerId VARCHAR(50),
CONSTRAINT CARD_PK PRIMARY KEY(CARDID),
CONSTRAINT CUSTOMER_Id_FK FOREIGN KEY (CustomerId) REFERENCES CUSTOMER(CustomerID)) ;
--------------------------------------------------------------------------------------------------------
CREATE TABLE SELECTORDER
( OrderID VARCHAR(50),
OrderName VARCHAR(50),
OrderPrice INT,
OrderQuantity INT,
CONSTRAINT SELECTORDER_PK PRIMARY KEY(OrderID));

SELECT * FROM SELECTORDER;
SELECT * FROM product;
