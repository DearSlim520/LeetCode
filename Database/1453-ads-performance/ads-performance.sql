# Write your MySQL query statement below

select ad_id,
       COALESCE(round(click_cnt / (click_cnt + view_cnt) * 100, 2), 0) as ctr
from (
    select ad_id,
        sum(case when action = 'Clicked' then 1 else 0 end) as click_cnt,
        sum(case when action = 'Viewed' then 1 else 0 end) as view_cnt
    from ads
    group by ad_id
) f
order by ctr desc, ad_id