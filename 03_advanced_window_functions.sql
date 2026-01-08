-- 03_advanced_window_functions.sql
WITH customer AS (
  SELECT
    o.user_id,
    MIN(o.order_time) AS first_order,
    MAX(o.order_time) AS last_order,
    COUNT(*) AS orders_count,
    SUM(p.price) AS total_spend
  FROM orders o
  JOIN order_products_prior op ON o.order_id = op.order_id
  JOIN products p ON op.product_id = p.product_id
  GROUP BY o.user_id
)
SELECT
  user_id,
  orders_count,
  total_spend,
  (total_spend / NULLIF(orders_count,0)) AS avg_order_value,
  DATE_PART('day', CURRENT_DATE - last_order) AS recency_days,
  DATE_PART('day', last_order - first_order) / NULLIF(orders_count-1,1) AS avg_days_between_orders
FROM customer
ORDER BY total_spend DESC
LIMIT 100;
