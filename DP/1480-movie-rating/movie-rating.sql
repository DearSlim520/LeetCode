# Write your MySQL query statement below

with cte_user as (
        select u.name, count(m.movie_id) as rating_cnt
        from movierating m
            left join users u
                 on m.user_id = u.user_id
        group by 1
),
     cte_movie as (
        select m.movie_id, v.title, avg(rating) as avg_rating
        from movierating m
            left join movies v
                on m.movie_id = v.movie_id
        where m.created_at between '2020-02-01' and last_day('2020-02-01')
        group by 1,2
     )
    (select name as results
    from cte_user
    order by rating_cnt desc, name
    limit 1)
    UNION ALL
    (select title as results
    from cte_movie
    order by avg_rating desc, title
    limit 1)