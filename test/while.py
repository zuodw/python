#encoding=utf-8
age_str = ''
age_int = 0
while age_int < 200:
	age_str = input('Please input your age: ')
	if age_str == 'quit':
		break
	
	age_int = int(age_str)
	if age_int < 3:
		print("You're free to see the movie")
	elif age_int >= 3 and age_int < 12:
		print('Your ticket price is $10')
	elif age_int >= 12:
		print('Your ticket price is $15')