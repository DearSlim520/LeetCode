# Write your MySQL query statement below

with cte_cnt as (
    select activity
          , count(name) as cnt
    from friends
    group by activity
), 
    cte_max_min as(
        select max(cnt) as max_cnt, 
               min(cnt) as min_cnt
        from cte_cnt
)
select c0.activity
from cte_cnt c0
    inner join cte_max_min c1
        on c0.cnt <> max_cnt
        and c0.cnt <> min_cnt