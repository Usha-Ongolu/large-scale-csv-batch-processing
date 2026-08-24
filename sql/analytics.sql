-- Revenue by country

SELECT
    Country,
    SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY Country
ORDER BY TotalRevenue DESC;


-- Revenue by category

SELECT
    Category,
    SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY Category
ORDER BY TotalRevenue DESC;


-- Monthly revenue

SELECT
    YEAR(OrderDate) AS SalesYear,
    MONTH(OrderDate) AS SalesMonth,
    SUM(Revenue) AS TotalRevenue
FROM Sales
GROUP BY
    YEAR(OrderDate),
    MONTH(OrderDate)
ORDER BY
    SalesYear,
    SalesMonth;
