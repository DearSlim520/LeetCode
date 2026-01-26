# Write your MySQL query statement below

WITH numbered AS (
    SELECT 
        log_id,
        ROW_NUMBER() OVER (ORDER BY log_id) AS rn
    FROM logs
)
SELECT 
    MIN(log_id)           AS start_id,
    MAX(log_id)           AS end_id
FROM (
    SELECT log_id, log_id - rn AS diff
    FROM numbered
) t
GROUP BY diff
ORDER BY start_id;
