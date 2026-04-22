USE northwind;
-- Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice FROM products;
-- Write a query to identify the products where the unit price is $7.50 or less. 
SELECT ProductID, ProductName, UnitPrice FROM products
WHERE UnitPrice >= 7.5;
-- What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
SELECT ProductID, ProductName, UnitPrice, UnitsInStock, UnitsOnOrder FROM products
WHERE UnitsInStock = 0 and UnitsOnOrder >= 1;

-- Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers? Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier
SELECT SupplierID, CompanyName FROM suppliers
WHERE CompanyName = "Tokyo Traders";
SELECT SupplierID, ProductID, ProductName FROM products
WHERE SupplierID = 4;

SELECT EmployeeID, FirstName, LastName FROM employees;
SELECT EmployeeID, FirstName, LastName, Title FROM employees
WHERE Title LIKE "%manager%" ;

