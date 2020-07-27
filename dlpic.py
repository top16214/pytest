#! /usr/bin/python
# coding:UTF-8

import sys, os
import urllib.request
import shutil
import csv


fake_UA = r"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"
dir_paths = []


def doDirs(mydir):
    '''make a new dir
    or delete an old dir'''
    mydir = os.path.join('../foto',mydir)

    if os.path.exists(mydir):
        shutil.rmtree(mydir, ignore_errors=True)
    
    os.mkdir(mydir)
    dir_paths.append(mydir)
    


def updateDB():
    '''把目录名写进csv文件
    '''
    
    if not os.path.exists("../foto/webpic.csv"):
        with open("../foto/webpic.csv", 'w') as fd:
                cfd = csv.writer(fd)
                cfd.writerow(['datetime', 'folder name', 'numbers'])
    
    with open("../foto/webpic.csv", 'a') as fd:
            cfd = csv.writer(fd)
            import time
            for item in dir_paths:
                mydir = os.path.basename(item)
                number = len(os.listdir(item))
                cfd.writerow([time.asctime(), mydir, number])

    


def testURL(file_path):
    """
    测试path中每行url的可用性
    """
    with open(file_path, encoding="utf-8") as fd:
        for line in fd:
            if line.startswith("http"):
                url = line
                # 只请求头部信息
                req = urllib.request.Request(url, method='HEAD')
                req.add_header("User-Agent", fake_UA)
                req.add_header("Referer",
                               r"https://www.jkforum.net/forum-603-1.html")
                r = urllib.request.urlopen(req)
                if r.status == 200:
                    print("{} OK".format(url))
                else:
                    print("{} not OK".format(url))

def down_file(url,cnt):
    """just download the URL to specified dir,
    the specified dir stores in the last element of dir_paths"""

    file_name = "%03d" % cnt + os.path.splitext(url)[-1]
    file_name = os.path.join(dir_paths[-1],file_name)
    
    def traditonalDown():
        '''下载失败的文件，利用传统方法再尝试下载'''
        req = urllib.request.Request(url, method='GET')
        req.add_header("User-Agent", fake_UA)
        req.add_header("Referer",r"https://www.jkforum.net/forum-603-1.html")
        try:
            r = urllib.request.urlopen(req)
            with open(file_name,mode="wb") as fd:
                fd.write(r.read())
        except:
            print(f'{url} download failed. Try to download it by setting proxy.')
            with open("downFailFiles.diz",mode='at+') as fd:
                fd.write(file_name)


    def reporthook(a, b, c):
        """
        显示下载进度
        :param a: 已经下载的数据块
        :param b: 数据块的大小
        :param c: 远程文件大小
        :return: None
        """
        print("\rdownloading: %5.1f%%" % (a * b * 100.0 / c), end="")

    urllib.request.urlretrieve(url,file_name,reporthook)


def readDList(file_path):
    '''doc'''
    with open(file_path,encoding='utf-8',newline='') as fd:
        for line in fd:
            line = line.strip()
            if line.startswith("http"):
                cnt += 1
                down_file(line, cnt)
            else:
                doDirs(line)
                cnt = 0     # cnt 是当前目录的图片张数，每次新建目录就重设为0，每下载一张图片就加1

    updateDB()

def main():
    try:
        file_path = sys.argv[1]
    except IndexError:
        while True:
            file_path = input("Input the path of download file:\t")
            if os.path.isfile(file_path):
                break
            else:
                print("{} file dosen't exist".format(file_path))
                continue

    # testURL(file_path)
    readDList(file_path)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
