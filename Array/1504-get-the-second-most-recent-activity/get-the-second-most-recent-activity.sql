# Write your MySQL query statement below

with cte_rank as (
        select *, row_number() over (partition by username order by startDate desc) as rn
        from useractivity
    ),
    cte_unique as (
        select *
        from useractivity
        group by username
        having count(*) = 1
    )
select username, activity, startDate, endDate
from cte_rank
where rn = 2
UNION ALL
select username, activity, startDate, endDate
from cte_unique