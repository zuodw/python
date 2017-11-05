#encoding=utf-8

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