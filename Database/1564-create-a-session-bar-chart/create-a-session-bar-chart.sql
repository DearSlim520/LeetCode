# Write your MySQL query statement below

with cte_bin as(
    select sum(case when duration between 0 and 299 then 1 else 0 end) as c1,
           sum(case when duration between 300 and 599 then 1 else 0 end) as c2,
           sum(case when duration between 600 and 899 then 1 else 0 end) as c3,
           sum(case when duration >= 900 then 1 else 0 end) as c4
    from sessions
    )
select '[0-5>' as bin, c1 as total from cte_bin
UNION ALL
select '[5-10>' as bin, c2 as total from cte_bin
UNION ALL
select '[10-15>' as bin, c3 as total from cte_bin
UNION ALL
select '15 or more' as bin, c4 as total from cte_bin


-- select case when duration between 0 and 299 then '[0-5>'
--             when duration between 303 and 599 then '[5-10>'
--             when duration between 600 and 899 then'[10-15>'
--             else '15 or more' end as bin,
--        COALESCE(count(session_id), 0) as total
-- from sessions
-- group by bin