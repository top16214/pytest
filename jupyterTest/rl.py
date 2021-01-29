#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import pycurl
import shutil

def download(url,savefile):
    savefile = savefile.rstrip()
    print(savefile)
    # with open(savefile, 'wb') as f:
        # c = pycurl.Curl()
        # c.setopt(c.URL, url)
        # c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36')
        # c.setopt(pycurl.FOLLOWLOCATION, True)
        # c.setopt(pycurl.MAXREDIRS,5)
        # c.setopt(c.WRITEDATA, f)
        # c.perform()
        # c.close()


def mkdir(dirname):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)  

    os.mkdir(dirname)
    cnt = 0
    return dirname
    
    
def main():
    FILENAME = r'./papa.lst'
    global cnt
    cnt = 0
    with open(FILENAME,'r',encoding='UTF-8') as foo:
        for line in foo:
           if(line.startswith("http")):
                filename = "".join([str(cnt),os.path.splitext(line)[-1]])
                savefile = dirname + os.path.sep + filename
                download(line,savefile)
                cnt += 1
           else:
                dirname = mkdir(line.rstrip())


def printsummary():
    pass

if __name__ == "__main__":
    main()