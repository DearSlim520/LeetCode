# Write your MySQL query statement below

with cte_orders_w_rn as (
        select o.seller_id, 
               o.item_id, 
               i.item_brand,
               row_number() over (partition by o.seller_id order by o.order_date) as rn
        from orders o
            left join items i
                on o.item_id = i.item_id
    )
select u.user_id as seller_id,
       case when COALESCE(c.item_brand, 'other') <> u.favorite_brand then 'no' else 'yes' end
        as 2nd_item_fav_brand
from users u
    left join cte_orders_w_rn c
        on u.user_id = c.seller_id
        and c.rn = 2