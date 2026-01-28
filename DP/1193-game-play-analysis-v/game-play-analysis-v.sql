# Write your MySQL query statement below

# by player + 1st event_date
with cte_day1 as (
        select player_id, 
               min(event_date) as day1
        from activity
        group by player_id
    ),
    cte_day1_n_2 as (
        select d.player_id,
               d.day1,
               a.event_date as day2,
               if(a.event_date is not null, 1, 0) as retention
        from cte_day1 d
            LEFT JOIN activity a
                ON d.player_id = a.player_id
                AND date_add(d.day1, interval 1 day) = a.event_date
    )
select day1 as install_dt,
       count(player_id) as installs,
       ROUND(sum(retention) / count(player_id), 2) as 'Day1_retention'
from cte_day1_n_2
group by 1
order by 1