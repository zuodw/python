#encoding=utf-8

from collections import OrderedDict

class Car(object):
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def getCarInfo(self):
		carInfo = str(self.year) + ' ' + self.make + ' ' + self.model
		return carInfo.title()

class EletricCar(Car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)

	def getCarInfo(self):
		carInfo = str(self.year) + ' ' + self.make + ' ' + self.model
		return carInfo.upper()

eCar = EletricCar('tesla', 'model s', 2016)
print(eCar.getCarInfo())



favorite_language = OrderedDict()
favorite_language['zuodw'] = 'python'
favorite_language['fanhx'] = 'ruby'
favorite_language['sylar'] = 'java'
favorite_language['peter'] = 'perl'

for key,value in favorite_language.items():
	print(key, value)
