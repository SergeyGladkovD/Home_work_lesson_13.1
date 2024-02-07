import json
import os


def load_data():
	"""Возвращает json файл."""
	with open(os.path.join('data', 'products.json'), 'r')as f:
		data = json.load(f)
		return data
