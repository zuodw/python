#coding=utf-8

def describe_pet(animal_type, pet_name):
	if isinstance(animal_type, str):
		print('str type:', animal_type)
	elif isinstance(animal_type, int):
		print('int type:', animal_type)

describe_pet('dog', 'Harry')
describe_pet(5, 'Harry')