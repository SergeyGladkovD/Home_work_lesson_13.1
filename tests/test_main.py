import pytest
from classes.classes import Category, Product


@pytest.fixture()
def random_category():
	return Category('Фрукты', 'Цитрусовые', ['Апельсины', 'Лимоны'])


def test_category_init(random_category):
	assert random_category.title == 'Фрукты'
	assert random_category.description == 'Цитрусовые'
	assert random_category.products == ['Апельсины', 'Лимоны']
	assert Category.count_of_categories == 1
	assert Category.count_of_unique_products == 2


@pytest.fixture()
def random_product():
	return Product('Апельсины', 'Мадагаскарские', 350.50, 100)


def test_product_init(random_product):
	assert random_product.title == 'Апельсины'
	assert random_product.description == 'Мадагаскарские'
	assert random_product.price == 350.50
	assert random_product.quantity_in_stock == 100
