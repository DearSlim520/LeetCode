# Write your MySQL query statement below


select sale_date,
    sum(case when fruit = 'apples' then sold_num
             when fruit = 'oranges' then -1 * sold_num end) as diff
from sales
group by sale_date
order by sale_date

