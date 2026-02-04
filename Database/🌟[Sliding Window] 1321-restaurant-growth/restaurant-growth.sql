# Write your MySQL query statement below

WITH daily AS (
    SELECT 
        visited_on,
        SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT d.visited_on,
       SUM(c.amount) as amount,
       ROUND(SUM(c.amount) / 7, 2) as average_amount
FROM daily d
    INNER JOIN daily c
        ON c.visited_on BETWEEN date_add(d.visited_on, INTERVAL -6 DAY)
                            AND d.visited_on
GROUP BY d.visited_on
HAVING COUNT(d.visited_on) >= 7
ORDER BY d.visited_on