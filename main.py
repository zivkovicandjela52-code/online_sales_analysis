from product import Product
from product_manager import ProductManager


def main():
    # Kreiranje ProductManager instance
    manager = ProductManager()

    # Kreiranje proizvoda
    p1 = Product("Laptop pro", 1200, 1)
    p2 = Product("Telefon x", 800, 2)
    p3 = Product("Tablet", 300, 7)

    # Dodavanje proizvoda u manager
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Prikaz svih proizvoda
    print("Lista proizvoda:")

    # Prikaz ukupne vrednosti inventara
    print("Ukupna vrednost inventara:", manager.total_inventory_value())


if __name__ == "__main__":
    main()