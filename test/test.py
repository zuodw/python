#coding=utf-8

class Car(object):
	def __init__(self, name, price=50):
		self.name = name
		self.price = price
		self.fuel = 0

	def showPrice(self):
		print(self.price)

	def setPrice(self, price):
		self.price = price

	def showName(self):
		print(self.name.title())

buick = Car('regal')

toyota = Car('camry', 15)

buick.showName()
print(buick.name)
buick.name = 'lacross'
buick.showPrice()
buick.showName()
buick.setPrice(30)
buick.showPrice()


toyota.showName()