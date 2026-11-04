from src.product import Product
from src.category_iterator import CategoryIterator
from src.category import Category

def test_iter(first_category):
    category_iterator = CategoryIterator(first_category)
    assert iter(category_iterator) is category_iterator

def test_next(first_category):
    category_iterator = CategoryIterator(first_category)
    result = next(category_iterator)
    assert result.name == '55" QLED 4K'


