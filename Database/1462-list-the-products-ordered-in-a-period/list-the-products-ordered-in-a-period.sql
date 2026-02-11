# Write your MySQL query statement below

select p.product_name,
       o.total_sale as unit
from (
    select product_id,
           sum(unit) as total_sale
    from orders
    where date_format(order_date, '%Y-%m') = '2020-02'
    group by product_id
) o
    INNER JOIN products p
        ON o.product_id = p.product_id
where o.total_sale >= 100