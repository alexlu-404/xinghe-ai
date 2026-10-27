##查询订单
from db import get_connection

def query_orders_by_customer(customer_code):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT o.order_no, o.order_date, o.status,
                       i.product_name, i.quantity, i.unit_price,
                       i.quantity * i.unit_price AS line_amount
                FROM sales_order o
                JOIN sales_order_items i ON i.order_id = o.id
                JOIN customers c ON c.id = o.customer_id
                WHERE c.customer_code = %s
                ORDER BY o.order_no, i.line_no;
                """,
                (customer_code,)
            )
            return cur.fetchall()
    finally:
        conn.close()

if __name__ == "__main__":
    rows = query_orders_by_customer("C2001")
    for row in rows:
        print(row)