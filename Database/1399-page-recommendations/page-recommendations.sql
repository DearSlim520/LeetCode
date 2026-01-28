# Write your MySQL query statement below

with cte_friend_list as (
    select if(user1_id = 1, user2_id, user1_id) as user_id
    from friendship
    where user1_id = 1 or user2_id = 1
)
select distinct l.page_id as recommended_page
from likes l
    inner join cte_friend_list f
        on l.user_id = f.user_id
    left join likes l2
        on l2.user_id = 1
        and l.page_id = l2.page_id
where l2.page_id is null