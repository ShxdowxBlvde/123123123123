from src.category import Category
from src.product import Product


def test_first_category_initialization(first_category):
    """Проверка корректности инициализации полей категории"""
    assert first_category.name == "Телевизоры"
    assert first_category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником"
    )


def test_category_counts_single(first_category):
    """Проверка корректной работы счетчиков для единичной категории"""
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_counts_multiple(first_category, second_category):
    """Проверка сквозного сложения счетчиков для нескольких категорий"""
    assert Category.category_count == 2
    assert Category.product_count == 5


def test_category_products_in_getter(first_category):
    """Проверяет вхождение конкретного имени продукта в геттер"""
    assert '55" QLED 4K' in first_category.products


def test_category_products_getter(first_category):
    """Тестируем геттер products на соответствие строгому шаблону с \n"""
    expected_output = (
        '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
        '61" OLED 4K, 83000.0 руб. Остаток: 9 шт.\n'
    )
    assert first_category.products == expected_output


def test_category_add_product(first_category):
    """Тестируем метод add_product и динамическое обновление геттера"""
    new_prod = Product("Тест-ТВ", "Описание", 50000.0, 2)
    first_category.add_product(new_prod)

    assert "Тест-ТВ, 50000.0 руб. Остаток: 2 шт.\n" in first_category.products


def test_category_counts(first_category):
    """Тестируем корректность работы счетчиков при инициализации и добавлении"""
    assert Category.category_count == 1
    assert Category.product_count == 2

    # Добавляем еще один товар через add_product
    new_prod = Product("Тест-ТВ", "Описание", 50000.0, 2)
    first_category.add_product(new_prod)

    # Проверяем, что счетчик продуктов увеличился на 1, а категорий остался прежним
    assert Category.category_count == 1
    assert Category.product_count == 3


# старые тесты но адаптированные под новые настройки доступа
def test_first_product_initialization(first_category):
    """Вместо извлечения объекта, проверяем, что данные первого продукта
    корректно отображаются в строке геттера
    """
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n' in first_category.products


def test_product_in_category(first_category):
    """Вместо индекса [0] проверяем ключевые факты о наличии товара
    в строковом представлении категории
    """
    products_string = first_category.products
    assert '55" QLED 4K' in products_string
    assert "Остаток: 7 шт." in products_string
