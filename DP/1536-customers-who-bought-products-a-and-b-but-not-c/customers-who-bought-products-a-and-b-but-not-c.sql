# Write your MySQL query statement below

with cte_ab as (
        select customer_id
        from orders
        where product_name in ('A','B')
        group by customer_id
        having count(distinct product_name) = 2
    ),
     cte_c as (
        select distinct customer_id
        from orders
        where product_name = 'C'
     )
select c.customer_id,
       c.customer_name
from customers c
    inner join cte_ab o1
        on c.customer_id = o1.customer_id
where o1.customer_id not in (select customer_id from cte_c)
order by 1