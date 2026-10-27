import json
import os
from src.category import Category
from src.product import Product


def read_json(path: str) -> list:
    abs_path = os.path.abspath(path)
    with open(abs_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data):
    categories = []
    for category_data in data:
        products_list = []
        for product_data in category_data["products"]:
            products_list.append(Product(**product_data))
        category_object = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products_list,
        )
        categories.append(category_object)
    return categories


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    products_data = create_objects_from_json(raw_data)
    print(products_data)
