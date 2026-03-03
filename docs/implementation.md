# Implementation Flow

## Creating a New Sales Order

### Step 1: User Input

User enters:

- Customer Name
- Total Order Value
- Total Collected
- Last Payment Date

---

### Step 2: Validation

System validates:

- Customer name is not empty
- Order value > 0
- Collected amount ≥ 0
- Collected amount ≤ Order value

---

### Step 3: Calculation

Outstanding Balance = Total Order Value - Total Collected

---

### Step 4: Database Transaction

Within a transaction:

1. Insert customer if not exists
2. Insert order record
3. Insert payment record (if collected > 0)

If any step fails → rollback transaction.

---

### Step 5: Confirmation

System displays confirmation message and updated dashboard data.

---

## Future Production API Design

Proposed endpoint:

POST /api/v1/orders

Example request:

```json
{
  "customer_name": "ABC Pvt Ltd",
  "order_value": 50000,
  "collected_amount": 30000,
  "payment_date": "2025-03-01"
}
