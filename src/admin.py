# admin.py

from data_manager import save_data

def admin_login(stored_password):
    entered_password = input("Enter admin password: ")
    return entered_password == stored_password

def set_admin_password(password):
    with open('data/admin_password.txt', 'w') as f:
        f.write(password)

def admin_dashboard(products, orders):
    while True:
        print("\nAdmin Dashboard")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. View Orders")
        print("6. Exit to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_products(products)
        elif choice == '2':
            add_product(products)
            save_data(products, orders)  # Save data after adding a product
        elif choice == '3':
            update_product(products)
            save_data(products, orders)  # Save data after updating a product
        elif choice == '4':
            delete_product(products)
            save_data(products, orders)  # Save data after deleting a product
        elif choice == '5':
            view_orders(orders)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def add_product(products):
    pid = input("Enter Product ID: ")
    if pid in products:
        print("Product ID already exists.")
        return
    name = input("Enter Product Name: ")
    price = float(input("Enter Product Price (in KES): "))  # Changed to KES
    quantity = int(input("Enter Product Quantity: "))
    category = input("Enter Product Category: ")  # New category field
    products[pid] = {'name': name, 'price': price, 'quantity': quantity, 'category': category}
    print("Product added successfully.")

def view_products(products):
    print("\nProduct List:")
    for pid, info in products.items():
        print(f"ID: {pid}, Name: {info['name']}, Price: KES {info['price']:.2f}, Quantity: {info['quantity']}, Category: {info['category']}")

def update_product(products):
    pid = input("Enter Product ID to update: ")
    if pid not in products:
        print("Product not found.")
        return
    name = input("Enter new Product Name (leave empty to keep current): ")
    if name:
        products[pid]['name'] = name
    price = input("Enter new Product Price (in KES, leave empty to keep current): ")
    if price:
        products[pid]['price'] = float(price)
    quantity = input("Enter new Product Quantity (leave empty to keep current): ")
    if quantity:
        products[pid]['quantity'] = int(quantity)
    category = input("Enter new Product Category (leave empty to keep current): ")
    if category:
        products[pid]['category'] = category
    print("Product updated successfully.")

def delete_product(products):
    pid = input("Enter Product ID to delete: ")
    if pid in products:
        del products[pid]
        print("Product deleted successfully.")
    else:
        print("Product not found.")



def view_orders(orders):
    print("\nOrder List:")
    for order in orders:
        customer_name = order.get('customer_name', 'Unknown')
        customer_phone = order.get('customer_phone', 'Unknown')
        order_details = order.get('order_details', {})
        total = order.get('total', 0)
        
        print(f"Customer Name: {customer_name}, Phone: {customer_phone}")
        for pid, item in order_details.items():
            print(f"  {item['quantity']} x {item['name']} @ KES {item['price']:.2f} each")
        print(f"Total: KES {total:.2f}")
        print("-------------------------------")