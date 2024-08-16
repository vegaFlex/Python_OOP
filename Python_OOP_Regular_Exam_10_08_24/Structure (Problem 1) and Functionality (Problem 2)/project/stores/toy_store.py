from project.stores.base_store import BaseStore
from collections import defaultdict


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return 'ToyStore'

    def store_stats(self):
        lines = []
        lines.append(f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}")
        lines.append(self.get_estimated_profit())
        lines.append("**Toys for sale:")

        if not self.products:
            return '\n'.join(lines)

        model_products = defaultdict(list)
        for product in self.products:
            model_products[product.model].append(product)

        for model in sorted(model_products):
            products = model_products[model]
            num_pieces = len(products)
            avg_price = sum(p.price for p in products) / num_pieces
            lines.append(f"{model}: {num_pieces}pcs, average price: {avg_price:.2f}")

        return '\n'.join(lines)