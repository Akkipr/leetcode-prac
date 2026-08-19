-- Last updated: 8/18/2026, 11:44:51 PM
# Write your MySQL query statement below
SELECT MAX(salary) as SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
)