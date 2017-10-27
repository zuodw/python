#coding: utf-8

bak_list = ['Power', 'DCU', 'MEU', 'DSRC']

m_list = [x + '、' +  y + '、' + z for x in bak_list for y in bak_list for z in bak_list if x != y and x != z and y != z]

for m in m_list:
	print(m)
	pass


# n_list = [x + '、' +  y for x in bak_list for y in bak_list if x != y]
# for n in n_list:
# 	print(n)