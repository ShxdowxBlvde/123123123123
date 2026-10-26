def test_category_initialization(first_category):
    assert first_category.name == "Телевизоры"
    assert (
        first_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(first_category.products) == 2


def test_product_in_category(first_category):
    product = first_category.products[0]
    assert product.name == '55" QLED 4K'
    assert product.quantity == 7


def test_category_counts_single(first_category):
    assert first_category.category_count == 1
    assert first_category.product_count == 2


def test_category_counts_multiple(first_category, second_category):
    assert first_category.category_count == 2
    assert first_category.product_count == 5
