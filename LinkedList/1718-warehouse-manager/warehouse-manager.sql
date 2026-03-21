# Write your MySQL query statement below

select w.name as warehouse_name,
       SUM(w.units * width * length * height) as volume
from warehouse w
    left join products p
        on w.product_id = p.product_id
group by 1
;