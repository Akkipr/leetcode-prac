-- Last updated: 8/20/2026, 6:00:13 PM
# Write your MySQL query statement below
SELECT score, (DENSE_RANK() OVER (ORDER BY score DESC)) AS "rank"
FROM Scores