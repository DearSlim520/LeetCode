# Write your MySQL query statement below

with cte_user as (
        select u.name
        from movierating m
            left join users u
                 on m.user_id = u.user_id
        group by 1
        order by count(m.movie_id) desc, u.name
        limit 1
),
     cte_movie as (
        select m.movie_id, v.title
        from movierating m
            left join movies v
                on m.movie_id = v.movie_id
        where m.created_at between '2020-02-01' and last_day('2020-02-01')
        group by 1,2
        order by avg(rating) desc, v.title
        limit 1
     )
    (select name as results
    from cte_user)
    UNION ALL
    (select title as results
    from cte_movie)