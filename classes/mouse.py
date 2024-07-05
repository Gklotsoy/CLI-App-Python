from classes.product import Product


class Mouse(Product):
    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
        self.category = "Mouse"

    def display_product(self):
        self.connect()
        sql = "Select * from tls_employee.public.products where category = 'Mouse'"
        self.execute(sql)
        result = self.cursor.fetchall()
        if result:
            print('Mouse:')
            for product in result:
                print(f'Mouse ID: {product[0]}')
                print(f'Mouse Name: {product[1]}')
                print(f'Mouse Price: {product[2]}')
                print(f'Mouse Stock: {product[3]}')
                print(f'Mouse Category: {product[4]}')
                print('------------------------------------')
        else:
            print('No Mouse found')

        print('------------------------------------')

        self.disconnect()

    def add_product(self):
        super().add_product()
        query = f"Insert into tls_employee.public.products (product_id, name, price, stock, category) values ('{self.product_id}', '{self.name}', {self.price}, {self.stock}, '{self.category}')"
        self.execute(query)

