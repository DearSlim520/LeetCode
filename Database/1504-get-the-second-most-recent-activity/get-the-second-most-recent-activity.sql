# Write your MySQL query statement below

with cte_rank as (
        select *, 
               row_number() over (partition by username order by startDate desc) as rn,
               count(*) over (partition by username) as cnt
        from useractivity
    )
select username, activity, startDate, endDate
from cte_rank
where rn = 2 or cnt = 1