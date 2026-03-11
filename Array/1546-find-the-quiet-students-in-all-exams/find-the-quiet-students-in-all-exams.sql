# Write your MySQL query statement below

with cte_high_low as (
        select exam_id,
            max(score) as highest,
            min(score) as lowest
        from exam
        group by exam_id
    ),
    non_silent_student as (
        select distinct student_id
        from exam e
            inner join cte_high_low c
                on e.exam_id = c.exam_id
                and e.score in (c.highest, c.lowest)
    )
select distinct e.student_id, s.student_name
from exam e
    inner join student s
        on e.student_id = s.student_id
where e.student_id not in (select student_id
                             from non_silent_student)
order by 1