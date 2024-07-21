# data_manager.py

import json
import os

PRODUCTS_FILE = 'data/products.json'
ORDERS_FILE = 'data/orders.json'
ADMIN_PASSWORD_FILE = 'data/admin_password.txt'

def load_data():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r') as f:
            products = json.load(f)
    else:
        products = {}
    
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'r') as f:
            orders = json.load(f)
    else:
        orders = []
    
    if os.path.exists(ADMIN_PASSWORD_FILE):
        with open(ADMIN_PASSWORD_FILE, 'r') as f:
            admin_password = f.read().strip()
    else:
        admin_password = None
    
    return products, orders, admin_password

def save_data(products, orders):
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump(products, f, indent=4)
    
    with open(ORDERS_FILE, 'w') as f:
        json.dump(orders, f, indent=4)
