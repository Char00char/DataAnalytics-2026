USE northwind;

-- What is the product name(s) of the most expensive products?
SELECT ProductName FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);

-- What is the product name(s) and categories of the least expensive products?
SELECT products.ProductName, categories.CategoryName FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);

-- What is the order id, shipping name and shipping address of all orders shipped via "Federal Shipping"?
SELECT orders.OrderID, orders.ShipName, orders.ShipAddress FROM orders
JOIN shippers 
ON orders.ShipVia = shippers.ShipperID
WHERE shippers.CompanyName = 'Federal Shipping';

-- What are the order ids of the orders that included "Sasquatch Ale"?

-- What is the name of the employee that sold order 10266?

-- What is the name of the customer that bought order 10266?