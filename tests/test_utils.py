import json
import pytest
from src.utils import read_json, create_objects_from_json
from src.category import Category


@pytest.fixture
def mock_json_file(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]
    file_path = tmp_path / "test_products.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return str(file_path)


def test_read_json(mock_json_file):
    """тестируем, что функция read_json корректно читает файл и возвращает list"""
    result = read_json(mock_json_file)

    assert isinstance(result, list)
    assert result[0]["name"] == "Смартфоны"
    assert result[0]["products"][0]["name"] == "Iphone 15"


def test_create_objects_from_json(mock_json_file):
    """тестируем, что функция создает правильные объекты"""
    Category.category_count = 0
    Category.product_count = 0

    raw_data = read_json(mock_json_file)
    categories = create_objects_from_json(raw_data)

    # проверяем структуру созданных объектов
    assert len(categories) == 1
    assert isinstance(categories[0], Category)
    assert categories[0].name == "Смартфоны"

    # проверяем вложенный продукт
    assert len(categories[0].products) == 1
    assert categories[0].products[0].name == "Iphone 15"
    assert categories[0].products[0].price == 210000.0

    # проверяем, что счетчики классов сработали корректно
    assert Category.category_count == 1
    assert Category.product_count == 1
