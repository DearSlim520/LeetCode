# Write your MySQL query statement below

select u.name,
       sum(t.amount) as balance
from transactions t
    inner join users u
        on t.account = u.account
group by 1
having sum(t.amount) > 10000;