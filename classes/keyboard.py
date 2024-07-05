from classes.product import Product


class Keyboard(Product):
    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
        self.category = "Keyboard"

    def display_product(self):
        self.connect()
        sql = "Select * from tls_employee.public.products where category = 'Keyboard'"
        self.execute(sql)
        result = self.cursor.fetchall()
        print('Keyboard:')

        if result:
            for product in result:
                print(f'Keyboard ID: {product[0]}')
                print(f'Keyboard Name: {product[1]}')
                print(f'Keyboard Price: {product[2]}')
                print(f'Keyboard Stock: {product[3]}')
                print(f'Keyboard Category: {product[4]}')
                print('------------------------------------')
        else:
            print('No Keyboard found')

        self.disconnect()

    def add_product(self):
        super().add_product()
        query = f"Insert into tls_employee.public.products (product_id, name, price, stock, category) values ('{self.product_id}', '{self.name}', {self.price}, {self.stock}, '{self.category}')"
        self.execute(query)

