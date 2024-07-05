import psycopg2
from classes.product import Product
from classes import *
from classes.monitor import Monitor
from classes.keyboard import Keyboard
from classes.mouse import Mouse
from classes.dbh import Dbh

while True:
    print("1. Add Product")
    print("2. Display Products")
    print("3. Other Actions")
    print("4. Exit")
    choice = input("Enter choice: ")
    print('------------------------------------')

    if choice == "1":
        while True:
            print("1. Add Monitor")
            print("2. Add Keyboard")
            print("3. Add Mouse")
            print("4. Exit")
            choice = input("Enter choice: ")
            print('------------------------------------')

            if choice == "1":
                try:
                    name = input("Enter Monitor Name: ")
                    price = float(input("Enter Monitor Price: "))
                    stock = int(input("Enter Monitor Stock: "))
                    monitor = Monitor(name, price, stock)
                    verify = input("Are you sure you want to add this product? (Y/N): ")
                    if verify == "Y" or verify == "y":
                        Product.add_product(monitor)
                        print()
                    else:
                        print("Product not added")
                        print()
                except ValueError:
                    print("Invalid input. Try again.")
                    print('------------------------------------')

            elif choice == "2":
                try:
                    name = input("Enter Keyboard Name: ")
                    price = float(input("Enter Keyboard Price: "))
                    stock = int(input("Enter Keyboard Stock: "))
                    keyboard = Keyboard(name, price, stock)
                    verify = input("Are you sure you want to add this product? (Y/N): ")
                    if verify == "Y" or verify == "y":
                        Product.add_product(keyboard)
                        print()
                    else:
                        print("Product not added")
                        print()
                except ValueError:
                    print("Invalid input. Try again.")
                    print('------------------------------------')

            elif choice == "3":
                try:
                    name = input("Enter Mouse Name: ")
                    price = float(input("Enter Mouse Price: "))
                    stock = int(input("Enter Mouse Stock: "))
                    mouse = Mouse(name, price, stock)
                    verify = input("Are you sure you want to add this product? (Y/N): ")
                    if verify == "Y" or verify == "y":
                        Product.add_product(mouse)
                        print()
                    else:
                        print("Product not added")
                        print()
                except ValueError:
                    print("Invalid input. Try again.")
                    print('------------------------------------')

            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.")
                print('------------------------------------')

    elif choice == "2":
        while True:
            print("1. Display Monitors")
            print("2. Display Keyboards")
            print("3. Display Mice")
            print("4. Display All Products")
            print("5. Search Product by ID")
            print("6. Exit")
            choice = input("Enter choice: ")
            print('------------------------------------')

            if choice == "1":
                monitor = Monitor(None, None, None)
                monitor.display_product()
                print('------------------------------------')
            elif choice == "2":
                keyboard = Keyboard(None, None, None)
                keyboard.display_product()
                print('------------------------------------')
            elif choice == "3":
                mouse = Mouse(None, None, None)
                mouse.display_product()
                print('------------------------------------')
            elif choice == "4":
                product = Product(None, None, None)
                product.display_product()
                print('------------------------------------')
            elif choice == "5":
                product_id = input("Enter Product ID: ")
                product = Product(None, None, None)
                product.search_product(product_id)
                print('------------------------------------')
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")
                print('------------------------------------')

    elif choice == "3":
        while True:
            print("1. Update Product")
            print("2. Delete Product")
            print("3. Exit")
            choice = input("Enter choice: ")
            print('------------------------------------')

            if choice == "1":
                product_id = input("Enter Product ID: ")
                product = Product(None, None, None)
                product.search_product(product_id)
                print('------------------------------------')
                # name = input("Enter Product Name: ")
                try:
                    price = float(input("Enter Product Price: "))
                    stock = int(input("Enter Product Stock: "))
                    product = Product(None, price, stock)
                    product.update_product(product_id)
                    print('------------------------------------')
                except ValueError:
                    print("Invalid input. Try again.")
                print('------------------------------------')
            elif choice == "2":
                product_id = input("Enter Product ID: ")
                product = Product(None, None, None)
                product.search_product(product_id)
                print('------------------------------------')
                product.delete_product(product_id)
                print('------------------------------------')
            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.")
                print('------------------------------------')

    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
