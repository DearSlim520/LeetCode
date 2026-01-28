# Write your MySQL query statement below

# by player + 1st event_date
with cte_rn as (
        select player_id, 
               event_date,
               row_number() over (partition by player_id order by event_date) as rn
        from activity
    ),
    cte_day1_n_2 as (
        select player_id,
               MAX(case when rn = 1 then event_date end) as day1,
               MAX(case when rn = 2 then event_date else null end) as day2
        from cte_rn
        where rn <= 2
        group by player_id
    ),
    cte_retention_by_player as(
        select player_id,
               day1,
               day2,
               if(day2 is not null and day2 - day1 = 1, 1, 0) as retention
        from cte_day1_n_2    
    )
select day1 as install_dt,
       count(player_id) as installs,
       ROUND(sum(retention) / count(player_id), 2) as 'Day1_retention'
from cte_retention_by_player
group by 1
order by 1