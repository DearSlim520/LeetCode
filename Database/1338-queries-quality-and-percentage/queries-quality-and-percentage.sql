# Write your MySQL query statement below

# new columns: quality, 
select query_name,
    --    position, 
    --    rating,
       ROUND(AVG(rating / position), 2) as quality,
       ROUND(SUM(case when rating < 3 then 1 else 0 end) / count(*) * 100, 2) as poor_query_percentage
from queries
group by query_name