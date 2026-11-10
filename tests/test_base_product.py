import pytest

from src.product import Product
from src.base_product import BaseProduct

def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()

def test_base_product_is_not_abstract():
    product = Product(
        "Samsung",
        "256GB",
        100000.0,
        5
    )
