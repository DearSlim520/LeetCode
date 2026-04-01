# Write your MySQL query statement below

with cte as(
        select customer_id,
            dense_rank() over (partition by customer_id order by count(order_id) desc) as rn,
            product_id
        from orders
        group by customer_id, product_id
)
select o.customer_id,
       o.product_id,
       p.product_name
from cte o
    inner join products p
        on o.product_id = p.product_id
where o.rn = 1