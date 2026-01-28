# Write your MySQL query statement below

# deal with weather: avg
# inner join for country name

with cte_country_avg as (
    select country_id,
           avg(weather_state) as avg_temp
    from weather
    where date_format(day, '%Y-%m') = '2019-11'
    group by 1
    )
select c.country_name,
       case when a.avg_temp <= 15 then 'Cold'
            when a.avg_temp >= 25 then 'Hot'
            else 'Warm' end                  as weather_type
from Countries c
    inner join cte_country_avg a
        on c.country_id = a.country_id
