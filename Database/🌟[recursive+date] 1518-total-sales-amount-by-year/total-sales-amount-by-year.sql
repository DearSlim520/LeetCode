with recursive cte_year as (
        select 2018 as yr
        UNION ALL
        select yr + 1
        from cte_year
        where yr <= 2019
    ),
    cte_dim_date as (
        select yr, 
               date(concat(yr, '-01-01')) as year_start, 
               date(concat(yr, '-12-31')) as year_end
        from cte_year
    ),
    cte_sales_date as (
        select s.product_id, 
               d.yr as report_year, 
               greatest(d.year_start, s.period_start) as effective_start,
               least(d.year_end, s.period_end) as effective_end,
               s.average_daily_sales
        from cte_dim_date d
            INNER JOIN sales s
                ON d.yr between year(s.period_start) and year(s.period_end)
    )
select c.product_id,
       p.product_name,
       cast(c.report_year as CHAR) as report_year,
       (datediff(c.effective_end, c.effective_start) + 1) * c.average_daily_sales as total_amount
from cte_sales_date c
    left join product p
        on c.product_id = p.product_id
where c.effective_end >= c.effective_start
order by c.product_id, c.report_year