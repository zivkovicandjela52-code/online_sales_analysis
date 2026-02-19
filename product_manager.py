class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def remove_product(self, product_name):
    for product in self.products:
        if product.name == product_name:
            self.products.remove(product)
            print("Proizvod uklonjen:", product_name)
            return
    print("Proizvod nije pronađen.")