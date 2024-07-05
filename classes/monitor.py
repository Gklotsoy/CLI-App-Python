from classes.product import Product


class Monitor(Product):
    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)
        self.category = "Monitor"

    def display_product(self):
        self.connect()
        sql = "Select * from tls_employee.public.products where category = 'Monitor'"
        self.execute(sql)
        result = self.cursor.fetchall()
        print('Monitor:')

        if result:
            for product in result:
                print(f'Monitor ID: {product[0]}')
                print(f'Monitor Name: {product[1]}')
                print(f'Monitor Price: {product[2]}')
                print(f'Monitor Stock: {product[3]}')
                print(f'Monitor Category: {product[4]}')
                print('------------------------------------')
        else:
            print('No Monitor found')

        self.disconnect()

    def add_product(self):
        super().add_product()
        query = f"Insert into tls_employee.public.products (product_id, name, price, stock, category) values ('{self.product_id}', '{self.name}', {self.price}, {self.stock}, '{self.category}')"
        self.execute(query)
