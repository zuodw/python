#encoding=utf-8
import os

current_path = os.getcwd()
create_new_file = os.path.join(current_path, 'test.txt')

if os.path.exists(create_new_file) == False:
	os.mknod(current_path)
	pass

print('判断是否是绝对路径 isabs()', os.path.isabs(current_path))