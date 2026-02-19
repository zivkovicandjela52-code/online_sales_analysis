from product import Product
from product_manager import ProductManager


def main():
    # Kreiranje ProductManager instance
    manager = ProductManager()

    # Kreiranje proizvoda
    p1 = Product("Laptop", 1000, 5)
    p2 = Product("Telefon", 500, 10)
    p3 = Product("Tablet", 300, 7)

    # Dodavanje proizvoda u manager
    manager.add_product(p1)
    manager.add_product(p2)
    manager.add_product(p3)

    # Prikaz svih proizvoda
    print("Lista proizvoda:")
    manager.display_all_products()

    # Prikaz ukupne vrednosti inventara
    print("Ukupna vrednost inventara:", manager.total_inventory_value())


if __name__ == "__main__":
    main()