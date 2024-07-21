def add_order(products, orders):
    cart = {}
    while True:
        print("\nAdd Order")
        print("Available Products:")
        for pid, info in products.items():
            print(f"Product ID: {pid}, Name: {info['name']}, Price: ${info['price']:.2f}")

        pid = input("Enter Product ID to add to cart (or 'done' to finish): ")
        if pid == 'done':
            break
        
        if pid in products:
            quantity = int(input(f"Enter quantity for product {products[pid]['name']}: "))
            if pid in cart:
                cart[pid] += quantity
            else:
                cart[pid] = quantity
        else:
            print("Product not found.")

    # Process the order
    total_amount = 0
    for pid, quantity in cart.items():
        product = products[pid]
        total_amount += product['price'] * quantity
        print(f"Product: {product['name']}, Quantity: {quantity}, Subtotal: ${product['price'] * quantity:.2f}")

    print(f"Total Amount Due: ${total_amount:.2f}")
    # Optionally, save the order or generate a receipt
