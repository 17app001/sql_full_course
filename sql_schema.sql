
-- 建立商品資料表
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    price DECIMAL(10,2)
);

-- 建立顧客資料表
CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(100)
);

-- 建立訂單資料表
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE RESTRICT
);

-- 插入商品範例資料
INSERT INTO products (name, price) VALUES 
('可樂', 25.00),
('泡麵', 35.00),
('麵包', 20.00);

-- 插入顧客範例資料
INSERT INTO customers (name, email) VALUES 
('小明', 'ming@example.com'),
('小美', 'mei@example.com');

-- 插入訂單範例資料
INSERT INTO orders (customer_id, product_id, quantity) VALUES
(1, 2, 3),   -- 小明買了3個泡麵
(2, 1, 1),   -- 小美買了1瓶可樂
(1, 1, 2);   -- 小明又買了2瓶可樂
