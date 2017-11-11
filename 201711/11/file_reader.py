#encoding=utf-8


with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)

with open('pi_digits.txt') as file_object:
	contents = file_object.readlines()
for line in contents:
	print(line.rstrip())

	# for line in file_object:
		# print(line.rstrip())

pi_string = ''

for line in contents:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))


with open('write.txt', 'w') as f:
	num = 100
	f.write(str(num))