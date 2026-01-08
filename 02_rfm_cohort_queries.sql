-- 02_rfm_cohort_queries.sql
WITH last_order AS (
  SELECT user_id, MAX(order_time) AS last_order_date
  FROM orders
  GROUP BY user_id
),
freq AS (
  SELECT user_id, COUNT(*) AS frequency
  FROM orders
  GROUP BY user_id
),
monetary AS (
  SELECT o.user_id, SUM(p.price) AS monetary
  FROM orders o
  JOIN order_products_prior op ON o.order_id = op.order_id
  JOIN products p ON op.product_id = p.product_id
  GROUP BY o.user_id
)
SELECT l.user_id,
       DATE_PART('day', CURRENT_DATE - l.last_order_date) AS recency_days,
       f.frequency,
       m.monetary
FROM last_order l
LEFT JOIN freq f USING (user_id)
LEFT JOIN monetary m USING (user_id)
ORDER BY m.monetary DESC
LIMIT 50;
