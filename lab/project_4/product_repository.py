from project_4.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for i in self.products:
            if i.name == product_name:
                return i

    def remove(self, product_name):
        for i in self.products:
            if i.name == product_name:
                self.products.remove(i)

    def __repr__(self):
        result = ''
        for i in self.products:
            result += f'{i.name}: {i.quantity}\n'
        return result.strip()


