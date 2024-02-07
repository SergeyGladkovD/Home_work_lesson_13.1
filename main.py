from utils.read_json import load_data
from classes.classes import Category, Product


def main():
	data = load_data()
	for category in data:
		instance = Category(category['name'], category['description'], category['products'])
		for i in category["products"]:
			product = Product(i['name'], i['description'], i['price'], i['quantity'])


if __name__ == '__main__':
	main()
