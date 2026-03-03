# Data Model Documentation

## 1. Design Principles

The data model follows:

- Third Normal Form (3NF)
- Strong referential integrity
- Clear separation of master and transactional data
- Financial accuracy constraints

---

## 2. Core Tables

### Customers (Master Data)

Stores unique customer records.

Key Fields:

- customer_id (Primary Key)
- name (Unique)
- created_at

Rules:

- No duplicate customer names
- Required before creating orders

---

### Orders (Transactional Data)

Stores sales transactions.

Key Fields:

- order_id (Primary Key)
- customer_id (Foreign Key → customers)
- total_amount
- order_date
- status

Rules:

- Cannot create order without valid customer
- Total amount must be positive

---

### Payments (Financial Tracking)

Tracks payments received against orders.

Key Fields:

- payment_id (Primary Key)
- order_id (Foreign Key → orders)
- amount_paid
- payment_date

Rules:

- Payment cannot exist without an order
- ON DELETE CASCADE ensures no orphan payments

---

## 3. Relationships

customers (1) → (N) orders  
orders (1) → (N) payments  

This ensures:

- No orphan payments
- No orders without customers
- Clear outstanding balance calculation

---

## 4. Data Integrity Controls

- CHECK constraints prevent negative values
- UNIQUE constraint prevents duplicate customers
- Foreign keys enforce relational consistency
- Transactions ensure atomic operations

This ensures accounting-level reliability.
