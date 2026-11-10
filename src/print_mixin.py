class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"({self.name},"
            f" {self.description},"
            f" {self.price},"
            f" {self.quantity})"
        )
