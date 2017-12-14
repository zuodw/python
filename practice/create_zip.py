import os
import zipfile
import asyncio

'''
将备份文件夹中所有文件及文件夹压缩至xxxx.zip
'''

path = r'F:\备份'

for month_dir in os.listdir(path):
    cur_month_dir = os.path.join(path, month_dir)
    for day_dir in os.listdir(cur_month_dir):
        cur_day_dir = os.path.join(cur_month_dir, day_dir)
        target_zip_name = day_dir + '.zip'
        print(target_zip_name)
        # 如果zip已经存在，跳出循环
        if os.path.exists(target_zip_name):
            continue

        target_zip_path = os.path.join(cur_day_dir, target_zip_name)
        print(target_zip_path)
        with zipfile.ZipFile(target_zip_path, 'x', zipfile.ZIP_STORED, True) as f:
            for root, dirs, files in os.walk(cur_day_dir):
                for file in files:
                    if file != os.path.split(target_zip_path)[1]:  # 排除掉.zip自身
                        # parameter_2 是为了不要把整个路径都压缩进去
                        f.write(os.path.join(root, file), os.path.join(root, file)[len(cur_day_dir):])
