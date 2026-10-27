-- 1. 客户表
CREATE TABLE customers (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_code VARCHAR(32) NOT NULL UNIQUE,
    customer_name VARCHAR(200) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (status IN ('active', 'inactive'))
);

-- 2. 商品表
CREATE TABLE products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_code VARCHAR(32) NOT NULL UNIQUE,
    product_name VARCHAR(200) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (status IN ('active', 'inactive'))
);

-- 3. 库存表
CREATE TABLE inventory (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL REFERENCES products(id),
    warehouse VARCHAR(50) NOT NULL DEFAULT 'main',
    quantity NUMERIC(12,2) NOT NULL DEFAULT 0,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (quantity >= 0),
    UNIQUE (product_id, warehouse)
);

-- 4. 销售订单主表（注意表名是 sales_order，单数）
CREATE TABLE sales_order (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_no VARCHAR(32) NOT NULL UNIQUE,
    customer_id BIGINT NOT NULL REFERENCES customers(id),
    order_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    status VARCHAR(20) NOT NULL DEFAULT 'draft',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (status IN ('draft', 'confirmed', 'shipped', 'completed', 'cancelled'))
);

-- 5. 销售订单明细表
CREATE TABLE sales_order_items (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    order_id BIGINT NOT NULL REFERENCES sales_order(id),
    line_no INTEGER NOT NULL,
    product_id BIGINT NOT NULL REFERENCES products(id),
    product_name VARCHAR(200) NOT NULL,
    quantity NUMERIC(12,2) NOT NULL,
    unit_price NUMERIC(12,2) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CHECK (line_no > 0),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0),
    UNIQUE (order_id, line_no)
);