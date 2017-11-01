def make_pizza(size, *args):
	print("\nMakeing a " + str(size) + 
		"-inch pizza with the following toppings:")
	for arg in args:
		print("- " + arg)

def my_sum(x, y=2):
	""" = no spaces """
	print(x + y)