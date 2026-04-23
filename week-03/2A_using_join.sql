Use northwind;

-- Create a single query to list the product id, product name, unit price and category name of all products. Order by category name and within that, by product name.
SELECT products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName FROM products
JOIN categories 
ON products.CategoryID = categories.CategoryID
ORDER BY CategoryName, ProductName;

-- Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. Order by product name.
SELECT products.ProductID, products.ProductName, products.UnitPrice, suppliers.CompanyName AS SupplierName FROM products
JOIN suppliers  
ON products.SupplierID = suppliers.SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

-- Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. Order by product name.
SELECT products.ProductID, products.ProductName, products.UnitPrice, categories.CategoryName, suppliers.CompanyName AS SupplierName FROM products 
JOIN categories  
ON products.CategoryID = categories.CategoryID
JOIN suppliers 
ON products.SupplierID = suppliers.SupplierID
ORDER BY ProductName;

-- Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to.
SELECT orders.OrderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName AS Shipper FROM orders
JOIN shippers 
ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = "Germany"
ORDER BY Shipper, ShipName;

-- Start from the same query as above (#4), but omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.
SELECT orders.ShipName, COUNT(*) AS OrderCount, shippers.CompanyName AS Shipper FROM orders
JOIN shippers
ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = "Germany"
GROUP BY ShipName, CompanyName
ORDER BY Shipper,ShipName;

-- Create a single query to list the order id, order date, ship name, ship address of all orders that included Sasquatch Ale.
-- -- SELECT 
--     o.OrderID, 
--     o.OrderDate, 
--     o.ShipName, 
--     o.ShipAddress
-- FROM Orders o
-- JOIN `Order Details` od
--     ON o.OrderID = od.OrderID
-- JOIN Products p
--     ON od.ProductID = p.ProductID
-- WHERE p.ProductName = 'Sasquatch Ale'
-- ORDER BY o.OrderDate;
