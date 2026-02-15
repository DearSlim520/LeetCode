# Write your MySQL query statement below

with cte_cnt as (
    select activity
          , count(name) as cnt
    from friends
    group by activity
)
select activity
from cte_cnt
where cnt <> (select max(cnt) from cte_cnt)
  and cnt <> (select min(cnt) from cte_cnt)