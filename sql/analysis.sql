-- 1. Total Revenue
SELECT 
    ROUND(SUM(price + freight_value), 2) AS total_revenue
FROM order_items;

-- 2. Monthly Revenue Trend
SELECT 
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
    ROUND(SUM(oi.price + oi.freight_value), 2) AS monthly_revenue
FROM orders o
JOIN order_items oi 
    ON o.order_id = oi.order_id
GROUP BY month
ORDER BY month;

-- 3. Top 10 Products by Revenue
SELECT 
    p.product_id,
    ROUND(SUM(oi.price + oi.freight_value), 2) AS product_revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_id
ORDER BY product_revenue DESC
LIMIT 10;

-- 4. Revenue by Product Category
SELECT 
    p.product_category_name,
    ROUND(SUM(oi.price + oi.freight_value), 2) AS category_revenue
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY category_revenue DESC;

-- 5. Payment Method Distribution
SELECT 
    payment_type,
    COUNT(*) AS number_of_payments,
    ROUND(SUM(payment_value), 2) AS total_payment_value
FROM payments
GROUP BY payment_type
ORDER BY total_payment_value DESC;

-- 6. Orders by State
SELECT 
    c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC;
