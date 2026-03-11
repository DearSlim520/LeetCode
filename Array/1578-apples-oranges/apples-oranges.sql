# Write your MySQL query statement below

with cte_adjust_sign as(
    select sale_date,
        case when fruit = 'apples' then sold_num
                when fruit = 'oranges' then -1 * sold_num end as sold_num
    from sales
)
select sale_date, sum(sold_num) as diff
from cte_adjust_sign
group by sale_date
order by sale_date