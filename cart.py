from product import Product


class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product: Product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def display_cart(self):
        if not self.cart_items:
            print("Korpa je prazna.")
            return

        print("Sadržaj korpe:")
        for product in self.cart_items:
            print(f"{product.name} - Cena: {product.price} - Količina: {product.quantity}")

    def total_cart_value(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def checkout(self):
        total = self.total_cart_value()
        print("Ukupan iznos za naplatu:", total)
        self.cart_items.clear()
        print("Korpa je ispražnjena.")