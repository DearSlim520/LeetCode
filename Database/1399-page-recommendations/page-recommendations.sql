# Write your MySQL query statement below

with cte_friend_list as (
    select if(user1_id = 1, user2_id, user1_id) as user_id
    from friendship
    where user1_id = 1 or user2_id = 1
)
select distinct page_id as recommended_page
from likes l
    inner join cte_friend_list f
        on l.user_id = f.user_id
where page_id not in (select page_id from likes where user_id = 1)