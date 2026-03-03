CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    total_amount DECIMAL(14,2) NOT NULL CHECK (total_amount >= 0),
    order_date DATE NOT NULL,
    status VARCHAR(50) DEFAULT 'CONFIRMED',

    CONSTRAINT fk_customer
        FOREIGN KEY(customer_id)
        REFERENCES customers(customer_id)
        ON DELETE RESTRICT
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    amount_paid DECIMAL(12,2) NOT NULL CHECK (amount_paid >= 0),
    payment_date DATE NOT NULL,

    CONSTRAINT fk_order
        FOREIGN KEY(order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE
);
