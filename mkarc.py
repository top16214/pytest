#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import zipfile
import pycurl

def chk_download_list_file():
    """不存在down.lst文件则退出程序"""
    FILE = "down.lst"    
    if not os.path.exists(FILE):
        print("\n{} does't exist!".format(FILE))
        os._exit(1)

class each_down_project():
    """每一个需要下载的项目，包括文件夹名称和图片的url"""
    def __init__(self,FName):
        folder_name = os.path.join(os.getcwd(),FName)
        



def main():
    # print("hello")
    chk_download_list_file()



if __name__ == "__main__":
    main()
