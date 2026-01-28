with cte_player_matches as (
    select first_player as player_id, first_score as score
    from matches
    UNION ALL
    select second_player as player_id, second_score as score
    from matches
),
cte_sum as (
    select c.player_id,
           p.group_id,
           sum(c.score) as total_score,
           row_number() over (partition by group_id order by sum(c.score) desc, player_id) as rn
    from cte_player_matches c
        left join players p on c.player_id = p.player_id
    group by 1, 2
)
select group_id, player_id
from cte_sum
where rn = 1