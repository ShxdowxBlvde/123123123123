import pytest
from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Фикстура автоматически сбрасывает счетчики класса перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def first_category():
    return Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться просмотром, "
            "станет вашим другом и помощником"
        ),
        products=[
            Product(
                name='55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            ),
            Product(
                name='61" OLED 4K',
                description="Звук как из саба",
                price=83000.0,
                quantity=9,
            ),
        ],
    )


@pytest.fixture
def second_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны как средство коммуникации",
        products=[
            Product(
                name="Samsung Galaxy S23 Ultra",
                description="256GB",
                price=180000.0,
                quantity=5,
            ),
            Product(
                name="Iphone 15",
                description="512GB",
                price=210000.0,
                quantity=8,
            ),
            Product(
                name="Xiaomi Redmi Note 11",
                description="1024GB",
                price=31000.0,
                quantity=14,
            ),
        ],
    )


@pytest.fixture
def product():
    """Фикстура для изолированного тестирования одного продукта"""
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def sample_product_dict():
    """Фикстура возвращает словарь для тестирования класс-метода"""
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def another_smartphone():
    return Smartphone(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8,
        98.2,
        "15",
        512,
        "Gray space",
    )


@pytest.fixture
def lawn_grass():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture
def another_lawn_grass():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
