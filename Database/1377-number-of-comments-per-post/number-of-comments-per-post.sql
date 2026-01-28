# Write your MySQL query statement below

select s.post_id,
       count(distinct s2.sub_id) as number_of_comments
from 
    (
        select distinct sub_id as post_id
        from submissions 
        where parent_id is null
    ) s
        left join submissions s2
            on s.post_id = s2.parent_id
group by 1
order by 1