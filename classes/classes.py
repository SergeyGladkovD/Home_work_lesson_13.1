class Category:
	"""Класс категория."""
	title: str
	description: str
	products: list

	count_of_categories = 0
	count_of_unique_products = 0
	list_cup = []

	def __init__(self, title, description, products):
		"""Метод для инициализации экземпляра класса."""
		self.title = title
		self.description = description
		self.products = products
		Category.count_of_categories += 1
		for product in products:
			if product not in Category.list_cup:
				Category.list_cup.append(product)
				Category.count_of_unique_products += 1


class Product:
	"""Класс продукт."""
	title: str
	description: str
	price: float
	quantity_in_stock: int

	def __init__(self, title, description, price, quantity_in_stock):
		"""Метод для инициализации экземпляра класса."""
		self.title = title
		self.description = description
		self.price = price
		self.quantity_in_stock = quantity_in_stock
