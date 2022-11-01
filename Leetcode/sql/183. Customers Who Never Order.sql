# Write your MySQL query statement below
SELECT name AS Customers
FROM Customers S
LEFT Join Orders A
On S.id = A.customerId
WHERE customerId IS NULL