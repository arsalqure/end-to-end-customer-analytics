-- 01_basic_kpis.sql
-- Monthly Active Users (MAU)
SELECT
  DATE_TRUNC('month', order_time::date) AS month,
  COUNT(DISTINCT user_id) AS mau
FROM orders
GROUP BY 1
ORDER BY 1;
