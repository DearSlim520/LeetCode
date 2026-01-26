# Write your MySQL query statement below

with cte_first_tier as (
    select employee_id
    from employees
    where manager_id = 1 and employee_id <> 1
     ),
     cte_second_tier as (
        select e.employee_id
        from employees e
            inner join cte_first_tier f
                on f.employee_id = e.manager_id
     ),
     cte_third_tier as (
        select e.employee_id
        from employees e
            inner join cte_second_tier s
                on s.employee_id = e.manager_id
     )
select employee_id from cte_first_tier
UNION ALL
select employee_id from cte_second_tier
UNION ALL
select employee_id from cte_third_tier