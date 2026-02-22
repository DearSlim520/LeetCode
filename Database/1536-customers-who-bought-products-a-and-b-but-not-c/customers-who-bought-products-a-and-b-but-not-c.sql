# Write your MySQL query statement below

select c.customer_id,
       c.customer_name
from customers c
    inner join orders o
        on c.customer_id = o.customer_id
group by c.customer_id
having sum(o.product_name = 'A') >= 1
   and sum(o.product_name = 'B') >= 1
   and sum(o.product_name = 'c') = 0
order by 1