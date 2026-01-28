# Write your MySQL query statement below

# by user&date : mobile, desktop, both

with cte_user_by_date as (
        select user_id,
               spend_date,
               sum(case when platform = 'mobile' then amount else 0 end) as mobile_amount,
               sum(case when platform = 'desktop' then amount else 0 end) as desktop_amount
        from spending
        group by 1, 2
    ),
    cte_both as (
        select user_id,
               spend_date,
               if(mobile_amount > 0 and desktop_amount > 0, 0, mobile_amount) as mobile_amount,
               if(mobile_amount > 0 and desktop_amount > 0, 0, desktop_amount) as desktop_amount,
               if(mobile_amount > 0 and desktop_amount > 0, mobile_amount + desktop_amount, 0) as both_amount
        from cte_user_by_date
    ),
    cte_by_date as(
        select spend_date,
               sum(mobile_amount) as total_mobile_amount,
               sum(desktop_amount) as total_desktop_amount,
               sum(both_amount) as total_both_amount,
               sum(case when mobile_amount > 0 then 1 else 0 end) as total_mobile_users,
               sum(case when desktop_amount > 0 then 1 else 0 end) as total_desktop_users,
               sum(case when both_amount > 0 then 1 else 0 end) as total_both_users
        from cte_both
        group by spend_date
    )
select spend_date, 
       'desktop' as platform, 
       total_desktop_amount as total_amount, 
       total_desktop_users as total_users
from cte_by_date
UNION ALL
select spend_date, 
       'mobile' as platform, 
       total_mobile_amount as total_amount, 
       total_mobile_users as total_users
from cte_by_date
UNION ALL
select spend_date, 
       'both' as platform, 
       total_both_amount as total_amount, 
       total_both_users as total_users
from cte_by_date