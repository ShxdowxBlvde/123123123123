from src.product import Product


def test_product_initialization(product):
    """Проверка базовой инициализации атрибутов"""
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_new_product_classmethod(sample_product_dict):
    """Тестируем создание объекта класса Product через класс-метод new_product"""
    product = Product.new_product(sample_product_dict)
    assert isinstance(product, Product)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter_valid():
    """Тестируем успешное изменение цены через сеттер (положительное значение)"""
    product = Product("Iphone 15", "512GB", 210000.0, 8)
    product.price = 195000.0
    assert product.price == 195000.0


def test_product_price_setter_invalid(capsys):
    """Тестируем валидацию сеттера при некорректной цене (<= 0)"""
    product = Product("Iphone 15", "512GB", 210000.0, 8)

    product.price = -100.0
    assert product.price == 210000.0
    captured = capsys.readouterr()
    assert "цена должна быть больше нуля" in captured.out

    product.price = 0
    assert product.price == 210000.0
    captured = capsys.readouterr()
    assert "цена должна быть больше нуля" in captured.out
