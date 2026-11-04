from src.category_iterator import CategoryIterator


def test_iter(first_category):
    category_iterator = CategoryIterator(first_category)
    assert iter(category_iterator) is category_iterator


def test_next(first_category):
    category_iterator = CategoryIterator(first_category)
    result = next(category_iterator)
    assert result.name == '55" QLED 4K'
