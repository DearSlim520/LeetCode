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
               greatest(d.year_start, s.period_start) as real_start,
               least(d.year_end, s.period_end) as real_end,
               s.average_daily_sales
        from cte_dim_date d
            CROSS JOIN sales s
    ),
    cte_calculate as (
        select product_id,
               report_year,
               datediff(real_end, real_start) + 1 as cnt,
               average_daily_sales
        from cte_sales_date
        where real_start <= real_end 
    )
select c.product_id,
       p.product_name,
       cast(c.report_year as CHAR) as report_year,
       c.cnt * c.average_daily_sales as total_amount
from cte_calculate c
    left join product p
        on c.product_id = p.product_id
order by c.product_id, c.report_year