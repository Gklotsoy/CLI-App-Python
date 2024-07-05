import uuid

from classes.dbh import Dbh


def generate_product_id():
    return str(uuid.uuid4())


class Product(Dbh):
    def __init__(self, name, price, stock):
        super().__init__()
        self.category = None
        self.name = name
        self.price = price
        self.stock = stock
        self.product_id = generate_product_id()

    def display_product(self):
        self.connect()
        sql = "Select * from tls_employee.public.products order by category asc"
        self.execute(sql)
        result = self.cursor.fetchall()
        print('''PRODUCTS:
        ''')

        if result:
            for product in result:
                print(f'Product ID: {product[0]}')
                print(f'Product Name: {product[1]}')
                print(f'Product Price: {product[2]}')
                print(f'Product Stock: {product[3]}')
                print(f'Product Category: {product[4]}')
                print('------------------------------------')
        else:
            print('No product found')
        self.disconnect()

    def add_product(self):
        super().connect()
        sql = f"Insert into tls_employee.public.products (product_id, name, price, stock, category) values ('{self.product_id}', '{self.name}', {self.price}, {self.stock}, '{self.category}')"
        self.execute(sql)
        if self.cursor.rowcount == 1:
            print("Product added successfully")
        else:
            print("Product not added")
        super().disconnect()

    def search_product(self, product_id):
        print()
        self.connect()
        sql = f"Select * from tls_employee.public.products where product_id = '{product_id}'"
        self.execute(sql)
        result = self.cursor.fetchone()
        if result:
            print(
                f"Product ID: {result[0]} \nProduct Name: {result[1]} \nProduct Price: {result[2]} \nProduct Stock: {result[3]} \nProduct Category: {result[4]}")
        else:
            print("Product not found")
        self.disconnect()

    def update_product(self, product_id):
        self.connect()
        sql = f"Update tls_employee.public.products set price = {self.price}, stock = {self.stock} where product_id = '{product_id}'"
        self.execute(sql)
        if self.cursor.rowcount == 1:
            print("Product updated successfully")
        else:
            print("Product not found")
        self.disconnect()

    def delete_product(self, product_id):
        self.connect()
        sql = f"Delete from tls_employee.public.products where product_id = '{product_id}'"
        self.execute(sql)
        if self.cursor.rowcount == 1:
            print("Product deleted successfully")
        else:
            print("Product not found")
        self.disconnect()
