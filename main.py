import db
from query import display_total_revenue, display_revenue_by_product, display_revenue_by_category, display_revenue_by_city, dispaly_total_orders, display_pending_orders, display_cancel_orders, display_successful_orders, display_successful_payment, display_pending_payment, display_inventory_level, out_of_stock_products
# from query import add_customer, add_category, add_product, add_order, add_payment


# print("Enter data!")
# print("Press 1 for Add customers")
# print("Press 2 for Add categories")
# print("Press 3 for Add products")
# print("Press 4 for Add orders")
# print("Press 5 for Add payments")
# action = int(input("Enter any number in 1-5:"))

# if action == 1 :
    
#     db_conn = db.mysqlconnect()
        
#     data = {
        
#     'first_name': input("Enter first_name:\n"),
#     'last_name': input("Enter last_name:\n"),
#     'email': input("Enter email:\n"), 
#     'phone_no': input("Enter phone_no:\n"),
#     'address': input("Enter address:\n"), 
#     'city': input("Enter city:\n"),
#     'country': input("Enter country:\n")
    
#     }
#     add_customer(db_conn, data)
#     print(f"New customer {data['first_name']} added successfully!")
#     db.disconnect(db_conn)
    
# elif action == 2:
    
#     db_conn = db.mysqlconnect()
#     data = {'name': input("Enter category name:\n")}
#     add_category(db_conn, data)
#     print(f"New category {data['name']} added successfully!")
#     db.disconnect(db_conn)
    
# elif action == 3 :
    
#     db_conn = db.mysqlconnect()
#     data = {'name': input("Enter product name:\n"),
#     'cat_id': input("Enter cat_id:\n"), 
#     'price' : int(input("Enter price:")),
#     'product_quantity': int(input("Enter product quantity:"))
#     }
#     add_product(db_conn, data)
#     print(f"New product {data['name']} added successfully!")
#     db.disconnect(db_conn)

# elif action == 4 :
    
    
#     db_conn = db.mysqlconnect()
#     data = {
#     'customer_id': input("Enter customer_id:\n"),
#     'order_date' : input("Enter order_date (YYYY-MM-DD):\n"),
#     'required_date' : input("Enter required_date (YYYY-MM-DD):\n"),
#     'status' : input("Enter status:\n"),
#     'total_amount' : int(input("Enter total_amount:\n")),
#     'city' : input("Enter city:\n"),
#     }
    

#     add_order(db_conn, data)
#     db.disconnect(db_conn)

# elif action == 5:
#     db_conn = db.mysqlconnect()
    
#     data = {
#         'order_id': int(input("Enter order_id:\n")),
#         'customer_id': int(input("Enter customer_id:\n")),
#         'amount': int(input("Enter amount:\n")),
#         'payment_date': input("Enter payment date (YYYY-MM-DD):\n"), 
#         'payment_status': input("Enter payment status:(Pending or Successfull)\n")
#     }
    
#     add_payment(db_conn, data)
#     db.disconnect(db_conn)
    
# else:
#     print("Please enter a number between 1 and 5.")
    
db_conn = db.mysqlconnect()  
display_total_revenue(db_conn)
db.disconnect(db_conn)
   
   
db_conn = db.mysqlconnect()  
display_revenue_by_product(db_conn)
db.disconnect(db_conn)
   
   
db_conn = db.mysqlconnect()  
display_revenue_by_category(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
display_revenue_by_city(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
dispaly_total_orders(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
display_pending_orders(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
display_cancel_orders(db_conn)
db.disconnect(db_conn)


db_conn = db.mysqlconnect()  
display_successful_orders(db_conn)
db.disconnect(db_conn)


db_conn = db.mysqlconnect()  
display_pending_payment(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
display_successful_payment(db_conn)
db.disconnect(db_conn)


db_conn = db.mysqlconnect()  
display_inventory_level(db_conn)
db.disconnect(db_conn)

db_conn = db.mysqlconnect()  
out_of_stock_products(db_conn)
db.disconnect(db_conn)