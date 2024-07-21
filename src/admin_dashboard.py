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
        elif choice == '3':
            update_product(products)
        elif choice == '4':
            delete_product(products)
        elif choice == '5':
            view_orders(orders)
        elif choice == '6':
            break  # Exit to the main menu
        else:
            print("Invalid choice. Please try again.")
