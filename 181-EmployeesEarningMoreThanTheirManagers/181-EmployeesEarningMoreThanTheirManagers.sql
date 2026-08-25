-- Last updated: 8/24/2026, 11:42:25 PM
# Write your MySQL query statement below
SELECT name as Employee
FROM Employee e
WHERE e.salary > (
    SELECT salary
    FROM Employee j
    WHERE e.managerId = j.id
)
