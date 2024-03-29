from abc import ABC, abstractmethod


class MixinRepr:

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		print(repr(self))

	def __repr__(self):
		return f'Добавлен товар {self.__dict__}'


class Category:
	""" Класс категория. """
	count_of_categories = 0
	count_of_unique_products = 0
	list_cup = []
	list_all_products = []

	def __init__(self, title: str, description: str, products: list):
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
		""" Выводит список товаров в формате. """
		list_all_products = []
		for product in self.__products:
			list_all_products.append(f'{product.title}, {product.price} руб. Остаток: {product.quantity_in_stock} шт.')
		return list_all_products

	@property
	def products(self):
		""" Возвращает приватное значение атрибута. """
		return self.__products

	def add_products(self, new_product):
		""" Добавляет новый продукт в список продуктов. """
		if new_product.quantity_in_stock == 0:
			raise ValueError('Товар с нулевым количеством не может быть добавлен.')
		elif isinstance(new_product, Product):
			self.__products.append(new_product)
		raise TypeError

	def average_price(self):
		try:
			avr_price = [i.price for i in self.__products]
			return sum(avr_price) / len(avr_price)
		except ZeroDivisionError:
			return 0

	def __str__(self):
		""" Вывод информации. """
		return f'{self.title}, количество продуктов: {len(self.products)} шт.'

	def __len__(self):
		""" Возвращает длину списка продуктов. """
		return len(self.products)


class AllProducts(ABC):
	@abstractmethod
	def __init__(self):
		pass

	@classmethod
	@abstractmethod
	def new_product(cls, *args, **kwargs):
		pass


class Product(AllProducts):
	""" Класс продукт. """

	def __init__(self, title: str, description: str, price: float, quantity_in_stock: int):
		self.title = title
		self.description = description
		self.__price = price
		self.quantity_in_stock = quantity_in_stock

	@classmethod
	def new_product(cls, list_all_products, title, description, price, quantity_in_stock):
		""" Создает товар и возвращает объект, который можно добавлять в список товаров. """
		new_product = cls(title, description, price, quantity_in_stock)
		if new_product in list_all_products:
			for product in list_all_products:
				if product.title == new_product.title:
					product.quantity_in_stock += new_product.quantity_in_stock
					if new_product.price > product.price:
						product.price = new_product.price
		else:
			list_all_products.append(new_product)
		return new_product

	@property
	def price(self):
		""" Возвращает приватное значение атрибута. """
		return self.__price

	@price.setter
	def price(self, price):
		""" Меняет или оставляет цену. """
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

	def __str__(self):
		""" Вывод информации. """
		return f'{self.title}, {self.price} руб. Остаток: {self.quantity_in_stock} шт.'

	def __len__(self):
		""" Возвращает количество продуктов. """
		return self.quantity_in_stock

	def __add__(self, other):
		""" Возвращает общую число сложения двух продуктов. """
		type_class = type(self)
		if isinstance(other, type_class):
			return self.price * self.quantity_in_stock + other.price * other.quantity_in_stock
		raise TypeError


class Smartphone(MixinRepr, Product):
	""" Подкласс смартфон. """

	def __init__(self, title, description, price, quantity_in_stock, efficiency, model, hdd, color):
		super().__init__(title, description, price, quantity_in_stock)
		self.efficiency = efficiency
		self.model = model
		self.hdd = hdd
		self.color = color


class LawnGrass(MixinRepr, Product):
	""" Подкласс трава газонная. """

	def __init__(self, title, description, price, quantity_in_stock, country_of_origin, germination_period, color):
		super().__init__(title, description, price, quantity_in_stock)
		self.country_of_origin = country_of_origin
		self.germination_period = germination_period
		self.color = color
