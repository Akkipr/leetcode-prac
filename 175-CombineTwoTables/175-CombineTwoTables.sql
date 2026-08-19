-- Last updated: 8/18/2026, 11:40:31 PM
# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId;