
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore
from project.stores.base_store import BaseStore
from project.products.base_product import BaseProduct
from collections import defaultdict


class FactoryManager:
    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type == 'Chair':
            product = Chair(model, price)
        elif product_type == 'HobbyHorse':
            product = HobbyHorse(model, price)
        else:
            raise Exception("Invalid product type!")

        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if any(store.name == name for store in self.stores):
            pass

        if store_type == 'FurnitureStore':
            store = FurnitureStore(name, location)
        elif store_type == 'ToyStore':
            store = ToyStore(name, location)
        else:
            raise Exception(f"{store_type} is an invalid type of store!")

        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        store_sub_type = 'Furniture' if isinstance(store, FurnitureStore) else 'Toys'

        matching_products = [p for p in products if p.sub_type == store_sub_type]

        if not matching_products:
            return "Products do not match in type. Nothing sold."

        for product in matching_products:
            store.products.append(product)
            if product in self.products:
                self.products.remove(product)

        store.capacity -= len(matching_products)
        total_price = sum(p.price for p in matching_products)
        self.income += total_price

        return f"Store {store.name} successfully purchased {len(matching_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        matching_products = [p for p in self.products if p.model == product_model]

        for product in matching_products:
            product.discount()

        return f"Discount applied to {len(matching_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)
        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        lines = []
        lines.append(f"Factory: {self.name}")
        lines.append(f"Income: {self.income:.2f}")
        lines.append("***Products Statistics***")
        lines.append(f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}")

        model_counts = defaultdict(int)
        for product in self.products:
            model_counts[product.model] += 1

        for model in sorted(model_counts):
            count = model_counts[model]
            lines.append(f"{model}: {count}")

        lines.append(f"***Partner Stores: {len(self.stores)}***")
        for store_name in sorted(store.name for store in self.stores):
            lines.append(store_name)

        return '\n'.join(lines)