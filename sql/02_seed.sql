- ============================================================
-- 测试数据：客户、商品、库存、订单
-- 注意：表名是 sales_order（单数），不是 sales_orders
-- ============================================================

-- 1. 客户
INSERT INTO customers (customer_code, customer_name, status)
VALUES ('C2001', 'XX公司', 'active');

-- 2. 商品（5个）
INSERT INTO products (product_code, product_name, status) VALUES
('P1001', 'Vt1', 'active'),
('P1002', 'Vt2', 'active'),
('P1003', 'Vt3', 'active'),
('P1004', 'Vt4', 'active'),
('P1005', 'Vt5', 'active');

-- 3. 库存（仓库统一用 main）
-- P1001 库存 3，订单要 4 —— 这是故意留的“库存不足”测试用例
INSERT INTO inventory (product_id, warehouse, quantity)
SELECT id, 'main', v.qty
FROM products
JOIN (VALUES
    ('P1001', 3),
    ('P1002', 2),
    ('P1003', 1),
    ('P1004', 0),
    ('P1005', 0)
) AS v(code, qty) ON products.product_code = v.code;

-- 4. 订单主表
INSERT INTO sales_order (order_no, customer_id, order_date, status)
SELECT 'SO3001', id, '2026-11-15 10:30:00', 'draft'
FROM customers
WHERE customer_code = 'C2001';

-- 5. 订单明细（1 行：P1001，数量 4，单价 150）
INSERT INTO sales_order_items (order_id, line_no, product_id, product_name, quantity, unit_price)
SELECT o.id, 1, p.id, 'Vt1', 4, 150
FROM sales_order o
JOIN products p ON p.product_code = 'P1001'
WHERE o.order_no = 'SO3001';