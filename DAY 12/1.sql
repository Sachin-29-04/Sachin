(1)
 select customer_id,sum(price)
 from (select customer_id,price from sales inner join menu where sales.product_id=menu.product_id) as x
 group by customer_id;

(2) 
select customer_id,count(distinct order_date) 
from sales 
group by customer_id;

(3)
select customer_id,product_name from 
sales as s
left join 
menu as m
on s.product_id=m.product_id
where order_date=(select min(order_date) from sales where customer_id=s.customer_id )  ;


(4)
SELECT product_name, p_count
FROM (
    SELECT product_id, COUNT(*) AS p_count
    FROM sales
    GROUP BY product_id
) AS x
JOIN menu m ON x.product_id = m.product_id
WHERE x.p_count = (
    SELECT MAX(p_count)
    FROM (
        SELECT product_id, COUNT(*) AS p_count
        FROM sales
        GROUP BY product_id
    ) AS y
);


(5)
SELECT
    s.customer_id,
    m.product_name,
    COUNT(*) AS p_count
FROM sales s
JOIN menu m ON
 s.product_id = m.product_id
GROUP BY s.customer_id, s.product_id, m.product_name
HAVING COUNT(*) = (
    SELECT MAX(p_count1)
    FROM (
        SELECT COUNT(*) AS p_count1
        FROM sales
        WHERE customer_id = s.customer_id
        GROUP BY product_id
    ) AS y
);



(6)
SELECT s.customer_id, m.product_name, s.order_date
FROM sales s
JOIN members mem
 ON s.customer_id = mem.customer_id
JOIN menu m 
ON s.product_id = m.product_id
WHERE s.order_date = (
    SELECT MIN(order_date)
    FROM sales
    WHERE customer_id = s.customer_id
      AND order_date > mem.join_date
);

(7)
SELECT s.customer_id, m.product_name, s.order_date
FROM sales s
JOIN members mem 
ON s.customer_id = mem.customer_id
JOIN menu m 
ON s.product_id = m.product_id
WHERE s.order_date = (
    SELECT MAX(order_date)
    FROM sales
    WHERE customer_id = s.customer_id
      AND order_date < mem.join_date
);

(8)
SELECT
    s.customer_id,
    SUM(m.price) AS t_amt
FROM sales s
JOIN members mem ON s.customer_id = mem.customer_id
JOIN menu m ON s.product_id = m.product_id
WHERE s.order_date < mem.join_date
GROUP BY s.customer_id;

(9)
 select customer_id,sum(case when m.product_name = 'sushi' then m.price*20 else m.price*10 end ) 
 from sales as s
 join menu as m
 on s.product_id=m.product_id
 group by customer_id;
 
(10)
select s.customer_id,sum(case when s.order_date between m.join_date and date_add(m.join_date,interval 6 day)
 then me.price*2
 end ) as total_points
 from sales s
 join members m on s.customer_id=m.customer_id
 join menu me on s.product_id = me.product_id
 group by s.customer_id;
 
