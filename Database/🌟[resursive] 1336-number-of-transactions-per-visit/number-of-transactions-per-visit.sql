# Write your MySQL query statement below

with RECURSIVE
     cte_transaction_cnt as (
        select user_id,
                transaction_date,
                count(*) as trans_cnt
        from transactions
        group by 1,2
    ),
     cte_visit_trans as (
        select v.user_id, v.visit_date,
               COALESCE(t.trans_cnt, 0) as transactions_count
        from visits v
            left join cte_transaction_cnt t
                on v.user_id = t.user_id
                and v.visit_date = t.transaction_date
     ),
      cte_trans_visits as (
        select transactions_count,
               count(*) as visits_count
        from cte_visit_trans
        group by transactions_count
      ),
      cte_max_trans as ( 
        select max(transactions_count) as max_trans
        from cte_trans_visits
      ),
      cte_left as (
        select 0 as transactions_count
        UNION ALL
        select l.transactions_count + 1
        from cte_left l
            cross join cte_max_trans m
        where l.transactions_count < m.max_trans
      )
select l.transactions_count,
       COALESCE(c.visits_count, 0) as visits_count
from cte_left l
    left join cte_trans_visits c
        on l.transactions_count = c.transactions_count
order by 1