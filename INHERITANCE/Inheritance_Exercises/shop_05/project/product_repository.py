from EXAM_PREPAR_30_06_24_Python_OOP_06_2024.EXam_Prep_30_06_24_Python_OOP_06_2024 import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        product = self.find(product_name)
        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        result = ''

        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"
        return result.strip()

            # products = "\n".join(f"{product.name}: {product.quantity}")
            # return products

