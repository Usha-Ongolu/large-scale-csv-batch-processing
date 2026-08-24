CREATE TABLE Sales (
    OrderID INT NOT NULL,
    CustomerID INT NOT NULL,
    CustomerName VARCHAR(200),
    Country VARCHAR(100),
    Product VARCHAR(200),
    Category VARCHAR(100),
    OrderDate DATE,
    Quantity INT,
    UnitPrice DECIMAL(18,2),
    Revenue DECIMAL(18,2)
);
