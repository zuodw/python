#encoding=utf-8

l = int(input('please input: '))
result = 0

if l <= 100000:
	result = 100000 * 0.1
elif l > 100000 and l <= 200000:
	result = 100000 * 0.1 + (l - 100000) * 0.075

print(result)