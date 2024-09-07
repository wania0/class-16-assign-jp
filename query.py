def add_category(db_conn, data):
    cur = db_conn.cursor()
    name = data['name']
    cur.execute(f"INSERT INTO category (name) VALUES ('{name}')")
    db_conn.commit()
    
def add_product(db_conn, data):
    cur = db_conn.cursor()
    name = data['name']
    cat_id = data['cat_id']
    price = data ['price']
    product_quantity = data ['product_quantity']
    cur.execute(f"INSERT INTO product (name, cat_id, price, product_quantity) VALUES ('{name}', '{cat_id}', '{price}', '{product_quantity}')")
    db_conn.commit()

def add_customer(db_conn, data):
    cur = db_conn.cursor()
    first_name = data ['first_name']
    last_name = data ['last_name']
    email = data ['email']
    phone_no = data ['phone_no']
    address = data ['address']
    city = data ['city']
    country = data ['country']
    cur.execute(
    f"""
    INSERT INTO customer 
    (first_name, last_name, email, phone_no, address, city, country) 
    VALUES ('{first_name}', '{last_name}', '{email}', '{phone_no}', '{address}', '{city}', '{country}')
    """)
    
    db_conn.commit()
    
def add_payment(db_conn, data):
    cur = db_conn.cursor()
    order_id = data['order_id']
    customer_id = data['customer_id']
    amount = data['amount']
    payment_date = data['payment_date']
    payment_status = data['payment_status']
    cur.execute(f"INSERT INTO payment (order_id, customer_id, amount, payment_date, payment_status) VALUES ('{order_id}', '{customer_id}', '{amount}', '{payment_date}','{payment_status}')")
    db_conn.commit()
    
def add_order(db_conn, data):
    cur = db_conn.cursor()
    customer_id = data['customer_id']
    order_date = data['order_date']
    required_date = data['required_date']
    status = data['status']
    total_amount = data['total_amount']
    city = data ['city']
    cur.execute(f"INSERT INTO orders (customer_id, order_date, required_date, status, total_amount, city) VALUES ('{customer_id}', '{order_date}', '{required_date}', '{status}', '{total_amount}', '{city}')")
    db_conn.commit()


def display_total_revenue(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT SUM(total_amount) AS total_revenue FROM Orders WHERE order_date BETWEEN '2024-09-01' AND '2024-09-30' order by total_revenue desc")
    result = cur.fetchone()
    print(f"\nTotal revenue of September 2024 is {result['total_revenue']}\n")
    cur.close()
    
def display_revenue_by_product(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT p.name, SUM(od.total_price) AS revenue_by_product FROM order_details od JOIN product p ON od.product_id = p.id GROUP BY p.id, p.name, p.cat_id order by revenue_by_product desc")
    result = cur.fetchall()
    print(f"Total revenue by each product is:\n")
    for item in result:
        print(item)
    print()
    cur.close()
    
def display_revenue_by_category(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT p.cat_id, SUM(od.total_price) AS revenue_by_category FROM order_details od JOIN product p ON od.product_id = p.id GROUP BY p.cat_id order by revenue_by_category desc")
    result = cur.fetchall()
    print(f"Total revenue by each category is:\n")
    for item in result:
        print(item)
    print()
    cur.close()
    
def display_revenue_by_city(db_conn):
    cur = db_conn.cursor()
    cur.execute("select city, sum(total_amount) as revenue_by_city  from orders group by city order by revenue_by_city desc")
    result = cur.fetchall()
    print(f"Total revenue by each city is:\n")
    for item in result:
        print(item)
    print()
    cur.close()

def dispaly_total_orders(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS total_orders FROM orders")
    result = cur.fetchall()
    print(result)
    cur.close()
    
def display_pending_orders(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS pending_orders FROM orders WHERE status = 'Pending'")
    result = cur.fetchall()
    print(result)
    cur.close()

def display_cancel_orders(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS cancelled_orders FROM orders WHERE status = 'Cancelled'")
    result = cur.fetchall()
    print(result)
    cur.close()
    
def display_successful_orders(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS successful_orders FROM orders WHERE status = 'Completed'\n")
    result = cur.fetchall()
    print(result)
    print()
    cur.close()
    
def display_pending_payment(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS pending_payments FROM payment WHERE payment_status = 'Pending'")
    result = cur.fetchall()
    print(result)
    
    cur.close()
    
def display_successful_payment(db_conn):
    cur = db_conn.cursor()
    cur.execute("SELECT COUNT(*) AS successful_payments FROM payment WHERE payment_status = 'Successfull'")
    result = cur.fetchall()
    print(result)
    print()
    cur.close()
    
def display_inventory_level(db_conn):
    cur = db_conn.cursor()
    print("IN-STOCK PRODUCTS")
    cur.execute("select name, stock_level from product where stock_level != 0 ;")
    result = cur.fetchall()
    for item in result:
        print(item)
    print()
    cur.close()
    
def out_of_stock_products(db_conn):
    cur = db_conn.cursor()
    print("OUT-STOCK PRODUCTS")
    cur.execute("SELECT COUNT(*) as out_of_stock FROM product WHERE stock_level = 0")
    result = cur.fetchall()
    print(result)
    cur.close()