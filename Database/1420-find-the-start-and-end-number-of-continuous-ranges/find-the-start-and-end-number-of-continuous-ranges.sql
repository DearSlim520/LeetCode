# Write your MySQL query statement below

with cte_island as(
        select log_id,
               log_id - row_number() over (order by log_id) as diff
        from logs
)
select min(log_id) as start_id,
       max(log_id) as end_id
from cte_island
group by diff
order by start_id
