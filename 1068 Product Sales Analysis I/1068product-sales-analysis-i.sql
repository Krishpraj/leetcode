# Write your MySQL query statement below

SELECT Product.product_name,Sales.year,Sales.Price
FROM Product 
JOIN Sales on Sales.product_id=Product.product_id
