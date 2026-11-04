
class CategoryIterator:
    def __init__(self, category):
        self._category = category
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self._category.products_list):
            raise StopIteration
        product = self._category.products_list[self.index]
        self.index += 1
        return product
