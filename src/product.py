class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity"),
        )

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("цена должна быть больше нуля")
        else:
            self.__price = new_price
