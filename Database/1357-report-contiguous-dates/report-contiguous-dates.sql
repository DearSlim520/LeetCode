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
    cte_diff as ( 
        select status, 
               event_date,
               datediff(event_date, '2018-12-31') - row_number() over (partition by status order by event_date) as diff
        from cte_prev
    )
select status as period_state, 
       min(event_date) as start_date,
       max(event_date) as end_date
from cte_diff
group by status, diff
order by start_date