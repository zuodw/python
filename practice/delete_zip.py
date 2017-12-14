import os, re

'''
删除备份文件夹中的.zip文件，例如0314.zip
'''

path = r'F:\备份'

for root, dirs, files in os.walk(path):
    for file in files:
        if re.match(r'[0-9][0-9][0-9][0-9].zip', file):
            os.remove(os.path.join(root, file))