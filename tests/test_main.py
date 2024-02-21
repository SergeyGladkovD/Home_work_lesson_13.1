import pytest

from classes.classes import Category, Product, Smartphone, LawnGrass


@pytest.fixture()
def random_category():
	return Category('Смартфоны',
					'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни',
					[
						{
							"name": "Samsung Galaxy C23 Ultra",
							"description": "256GB, Серый цвет, 200MP камера",
							"price": 180000.0,
							"quantity": 5
						}])


def test_category_init(random_category):
	assert random_category.title == 'Смартфоны'
	assert random_category.description == 'Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
	assert random_category.products == [
		{
			"name": "Samsung Galaxy C23 Ultra",
			"description": "256GB, Серый цвет, 200MP камера",
			"price": 180000.0,
			"quantity": 5
		}]

	assert Category.count_of_categories == 1
	assert Category.count_of_unique_products == 1


@pytest.fixture()
def random_product():
	return Product('Iphone 15', '512GB, Gray space', 210000.0, 8)


def test_product_init(random_product):
	assert random_product.title == 'Iphone 15'
	assert random_product.description == '512GB, Gray space'
	assert random_product.price == 210000.0
	assert random_product.quantity_in_stock == 8


@pytest.fixture()
def random_smartphone():
	return Smartphone('Iphone 15', '512GB, Gray space', 210000.0, 8, 'Good', '15', '512GB', 'Gray space')


def test_smartphone_init(random_smartphone):
	assert random_smartphone.title == 'Iphone 15'
	assert random_smartphone.description == '512GB, Gray space'
	assert random_smartphone.price == 210000.0
	assert random_smartphone.quantity_in_stock == 8
	assert random_smartphone.efficiency == 'Good'
	assert random_smartphone.model == '15'
	assert random_smartphone.hdd == '512GB'
	assert random_smartphone.color == 'Gray space'


@pytest.fixture()
def random_grass():
	return LawnGrass('Газон', 'Трава газонная', 100.50, 200, 'Россия', '3 месяца', 'Зеленый')


def test_lawn_grass(random_grass):
	assert random_grass.title == 'Газон'
	assert random_grass.description == 'Трава газонная'
	assert random_grass.price == 100.50
	assert random_grass.quantity_in_stock == 200
	assert random_grass.country_of_origin == 'Россия'
	assert random_grass.germination_period == '3 месяца'
	assert random_grass.color == 'Зеленый'
