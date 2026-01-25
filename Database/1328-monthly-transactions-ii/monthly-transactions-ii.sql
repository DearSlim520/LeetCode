# Write your MySQL query statement below
with cte_main as (
    select * 
    from transactions
    where state = 'approved'
    UNION ALL
    select t.id,
           t.country,
           'chargeback' as state,
           t.amount,
           c.trans_date
    from transactions t
        inner join chargebacks c
            on t.id = c.trans_id
)
select date_format(trans_date, '%Y-%m') as month,
       country,
       sum(case when state = 'approved' then 1 else 0 end) as approved_count,
       sum(case when state = 'approved' then amount else 0 end) as approved_amount,
       sum(case when state = 'chargeback' then 1 else 0 end) as chargeback_count,
       sum(case when state = 'chargeback' then amount else 0 end) as chargeback_amount
from cte_main
group by date_format(trans_date, '%Y-%m'),
         country