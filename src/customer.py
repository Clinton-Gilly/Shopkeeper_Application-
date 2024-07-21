# customer.py

from admin import view_products
from data_manager import save_data

def customer_dashboard(products, orders):
    while True:
        print("\nCustomer Dashboard")
        print("1. View Products")
        print("2. Place Order")
        print("3. Exit to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_products(products)
        elif choice == '2':
            place_order(products, orders)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def place_order(products, orders):
    order = {}
    total = 0
    
    while True:
        pid = input("Enter Product ID to add to cart (or 'done' to finish): ")
        if pid == 'done':
            break
        if pid not in products:
            print("Product not found.")
            continue
        quantity = int(input(f"Enter quantity for {products[pid]['name']}: "))
        if quantity > products[pid]['quantity']:
            print(f"Only {products[pid]['quantity']} available.")
            continue
        if pid in order:
            order[pid]['quantity'] += quantity
        else:
            order[pid] = {
                'name': products[pid]['name'],
                'price': products[pid]['price'],
                'quantity': quantity
            }
        total += products[pid]['price'] * quantity
        print(f"Added {quantity} of {products[pid]['name']} to cart. Total is now KES {total:.2f}.")
    
    if order:
        print("\nOrder Summary:")
        for pid, item in order.items():
            print(f"{item['quantity']} x {item['name']} @ KES {item['price']:.2f} each")
        print(f"Total: KES {total:.2f}")
        
        # Collect customer details
        customer_name = input("Enter your name: ")
        customer_phone = input("Enter your phone number: ")
        
        orders.append({
            'customer_name': customer_name,
            'customer_phone': customer_phone,
            'order_details': order,
            'total': total
        })
        
        for pid, item in order.items():
            products[pid]['quantity'] -= item['quantity']
        
        save_data(products, orders)  # Save data after placing order
        print("Order placed successfully.")
    else:
        print("No items in the order.")
