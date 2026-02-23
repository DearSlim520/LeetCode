# Write your MySQL query statement below


select e.left_operand,
        e.operator,
        e.right_operand,
        case when e.operator = '>' then if(vl.value > vr.value, 'true', 'false')
            when e.operator = '=' then if(vl.value = vr.value, 'true', 'false')
            when operator = '<' then if(vl.value < vr.value, 'true', 'false') end as value
from expressions e
    left join variables vl
        on e.left_operand = vl.name
    left join variables vr
        on e.right_operand = vr.name