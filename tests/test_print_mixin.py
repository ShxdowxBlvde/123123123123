from src.product import Product


def test_product_repr():
    product = Product("Samsung", "256GB", 100000.0, 5)
    expected = "Product(Samsung, 256GB, 100000.0, 5)"
    assert repr(product) == expected


def test_print_mixin_output(capsys):
    product = Product("Samsung", "256GB", 100000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == ("Product(Samsung, 256GB, 100000.0, 5)")
