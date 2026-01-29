# Write your MySQL query statement below

with cte_prev as (
        select 'failed' as status,
                fail_date as event_date,
                COALESCE(lag(fail_date) over (order by fail_date), '1900-01-01') as prev_event_date
        from failed
        where year(fail_date) = '2019'
        UNION ALL
        select 'succeeded' as status,
                success_date as event_date,
                COALESCE(lag(success_date) over (order by success_date), '1900-01-01') as prev_event_date
        from succeeded
        where year(success_date) = '2019'
    ),
    cte_island as (
        select status,
               event_date,
               sum(case when datediff(event_date, prev_event_date) > 1 then 1 else 0 end) over (order by event_date asc) as island,
               row_number() over (order by event_date) as rn
        from cte_prev
    )
select status as period_state, 
       min(event_date) as start_date,
       max(event_date) as end_date
from cte_island
group by island
