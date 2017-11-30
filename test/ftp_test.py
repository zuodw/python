#encoding=utf-8

import os
from datetime import datetime

# FTP路径
FTP_PATH = r'Z:\To_HLX'
# 提供受託情報一覧(両備からHLXへ).xlsx 路径
EXCEL_PATH = r'C:\Users\zuodw\Desktop'


def getFTPFile():
    ftp_today_path = os.path.join(FTP_PATH, datetime.now().strftime('%Y%m%d'))
    files = os.listdir(ftp_today_path)
    return files



def writeFTPFilesToExcel():
    pass


if __name__ == '__main__':
    # 取得FTP下的所有文件夹，路径：Z:\To_HLX
    getFTPFile()
    pass