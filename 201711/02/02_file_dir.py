#encoding=utf-8

import os

'''
""" 可以根据不同系统环境，作成不同的路径字符串 """
s = os.path.join('home', 'rs', 'zuodawei', 'test.txt')

print(s)

""" 路径拆成2部分，后一部分总是最后级别的目录或者文件名 """
sp = os.path.split(s)
print(sp)

""" 取得文件扩展名,返回一个tuple，用[1]可以取得扩展名 """
ms = os.path.splitext(s)
print(ms[1])


'''
current_path = os.path.abspath('.')
print(current_path)

mk_dir_path = os.path.join(current_path, 'testDir')
mk_dir_rename = os.path.join(current_path, 'testDirRename')

if os.path.exists(mk_dir_path) == False:
	os.mkdir(mk_dir_path)

if os.path.exists(mk_dir_path) == True:
	os.rename(mk_dir_path, mk_dir_rename)

""" remove()权限不足 """
'''
if os.path.exists(mk_dir_rename) == True:
	os.remove(mk_dir_rename)
'''

print(os.listdir(os.getcwd()))