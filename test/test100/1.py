#encoding=utf-8

'''
num_list = [1,2,3,4]
result_list = []

for x in num_list:
	for y in num_list:
		for z in num_list:
			if x != y and x != z and y != z:
				result_list.append(x * 100 + y * 10 + z)
print(result_list)
print(len(result_list))
'''
print([x*100+y*10+z for x in range(1,5) for y in range(1,5) for z in range(1,5) if x != y and y != z and x != z])


