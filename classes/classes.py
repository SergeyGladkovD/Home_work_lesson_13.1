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
		self.__products = products
		Category.count_of_categories += 1
		for product in products:
			if product not in Category.list_cup:
				Category.list_cup.append(product)
				Category.count_of_unique_products += 1

	@property
	def all_products(self):
		"""Выводит список товаров в формате."""
		list_all_products = []
		for product in self.__products:
			list_all_products.append(f'{product.title}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.')
		return list_all_products

	@property
	def products(self):
		"""Возвращает приватное значение атрибута"""
		return self.__products

	def add_products(self, products):
		"""Добавляет новый продукт в список продуктов."""
		self.__products.append(products)


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
		self.__price = price
		self.quantity_in_stock = quantity_in_stock

	@classmethod
	def new_product(cls, list_all_products,  title, description, price, quantity_in_stock):
		"""Создает товар и возвращает объект, который можно добавлять в список товаров."""
		new_product = cls(title, description, price, quantity_in_stock)
		for product in list_all_products:
			if product.title == new_product.title:
				product.quantity_in_stock += new_product.quantity_in_stock
				if new_product.price > product.price:
					product.price = new_product.price
		return new_product

	@property
	def price(self):
		"""Возвращает приватное значение атрибута"""
		return self.__price

	@price.setter
	def price(self, price):
		if price > self.__price:
			self.__price = price
		elif price <= 0:
			print('Цена введена некорректно.')
		else:
			response = input('Новая цена ниже предыдущей, установить новую цену ("y" значит yes) или ("n" значит no)')
			if response == 'y':
				self.__price = price
			else:
				print('Цена осталась прежней.')
