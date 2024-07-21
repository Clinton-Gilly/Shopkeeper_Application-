# main.py

from admin import admin_dashboard, admin_login, set_admin_password
from customer import customer_dashboard
from data_manager import load_data, save_data

def main():
    products, orders, admin_password = load_data()
    
    # Set default password if none exists
    if admin_password is None:
        print("Setting default admin password to 'admin'.")
        set_admin_password('admin')
        admin_password = 'admin'
    
    while True:
        print("\nWelcome to the Shop Management System")
        print("1. Admin Dashboard")
        print("2. Customer Dashboard")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            if admin_login(admin_password):
                admin_dashboard(products, orders)
            else:
                print("Incorrect password.")
        elif choice == '2':
            customer_dashboard(products, orders)
        elif choice == '3':
            save_data(products, orders)  # Save data before exiting
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
