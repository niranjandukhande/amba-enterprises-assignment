from datetime import datetime

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Amba ERP Prototype", layout="wide")

st.title("Amba Enterprises ERP - Customer Financial Dashboard")


@st.cache_data
def load_data():
    return pd.read_excel("sample_customer_report.xlsx")


df = load_data()

st.subheader("Customer Financial Summary")
st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Create New Sales Order")

with st.form("order_form"):
    customer_name = st.text_input("Customer Name")
    order_value = st.number_input("Total Order Value ($)", min_value=0.0, step=100.0)
    collected_amount = st.number_input(
        "Amount Collected ($)", min_value=0.0, step=100.0
    )
    payment_date = st.date_input("Payment Date", datetime.today())

    submit = st.form_submit_button("Submit Order")

if submit:
    if not customer_name:
        st.error("Customer name is required.")
    elif order_value <= 0:
        st.error("Order value must be greater than 0.")
    elif collected_amount > order_value:
        st.error("Collected amount cannot exceed order value.")
    else:
        outstanding_balance = order_value - collected_amount

        st.success("Order validated successfully!")
        st.markdown(f"**Outstanding Balance:** $ {outstanding_balance:,.2f}")

        sql_statement = f"""
-- Insert into customers (if new)
INSERT INTO customers (name)
VALUES ('{customer_name}')
ON CONFLICT (name) DO NOTHING;

-- Insert into orders
INSERT INTO orders (customer_id, total_amount, order_date, status)
VALUES (
    (SELECT customer_id FROM customers WHERE name = '{customer_name}'),
    {order_value},
    '{payment_date}',
    'CONFIRMED'
);

-- Insert payment record
INSERT INTO payments (order_id, amount_paid, payment_date)
VALUES (
    LAST_INSERT_ID(),
    {collected_amount},
    '{payment_date}'
);
"""

        st.code(sql_statement, language="sql")

st.divider()
st.caption("Amba ERP Dashboard | Built by Niranjan Dukhande")
