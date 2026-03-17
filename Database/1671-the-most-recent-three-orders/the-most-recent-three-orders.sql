# Write your MySQL query statement below

with cte_rn as (
    select order_id, 
           order_date, 
           customer_id, 
           row_number() over (partition by customer_id order by order_date desc) as rn
    from orders
)
select c.name as customer_name,
       c.customer_id,
       r.order_id,
       r.order_date
from customers c
    inner join cte_rn r
        on c.customer_id = r.customer_id 
where r.rn <= 3
order by 1, 2, 4 desc