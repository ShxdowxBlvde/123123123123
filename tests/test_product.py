from src.product import Product, Smartphone, LawnGrass
import pytest


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


def test_str(product):
    result = str(product)
    assert result == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_products(second_category):
    products = second_category.products_list

    assert products[0] + products[1] == 2580000
    assert products[0] + products[2] == 1334000
    assert products[1] + products[2] == 2114000


def test_add_invalid_type(product):
    with pytest.raises(TypeError):
        product + "Телефон"


def test_add_smartphones(smartphone, another_smartphone):
    assert smartphone + another_smartphone == 2580000.0


def test_add_lawn_grass(lawn_grass, another_lawn_grass):
    assert lawn_grass + another_lawn_grass == 16750.0


def test_add_different_product_classes(smartphone, lawn_grass):
    with pytest.raises(TypeError):
        smartphone + lawn_grass


def test_add_product_and_smartphone(product, smartphone):
    with pytest.raises(TypeError):
        product + smartphone


def test_smartphone_repr():
    smartphone = Smartphone(
        "Samsung", "256GB", 100000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    expected = "Smartphone(Samsung, 256GB, 100000.0, 5)"

    assert repr(smartphone) == expected


def test_lawn_grass_repr():
    grass = LawnGrass("Газонная трава", "Для сада", 500.0, 20, "Россия", 7, "Зеленый")

    expected = "LawnGrass(Газонная трава, Для сада, 500.0, 20)"

    assert repr(grass) == expected


def test_subclasses_inherit_base_product():
    smartphone = Smartphone(
        "Samsung", "256GB", 100000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )

    grass = LawnGrass("Газонная трава", "Для сада", 500.0, 20, "Россия", 7, "Зеленый")

    assert isinstance(smartphone, Product)
    assert isinstance(grass, Product)
