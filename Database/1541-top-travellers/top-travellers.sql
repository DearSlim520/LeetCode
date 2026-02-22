# Write your MySQL query statement below

select name,
        travelled_distance
from (
    select u.name,
        u.id,
        COALESCE(SUM(r.distance), 0) as travelled_distance
    from users u 
        left join rides r
            on u.id = r.user_id
    group by u.name, u.id
    ) t
order by travelled_distance desc,
         name