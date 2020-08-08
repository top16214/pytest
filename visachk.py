#!/usr/bin/env python
# -*-coding:utf-8 -*-

from bs4 import BeautifulSoup, NavigableString, Tag
import urllib.request
import os, sys
import csv, time
import hashlib


def createCSV(alert_text):
    '''csv文件不存在，新建一个，把本次alert info录入'''
    with open("visaAlert.csv", mode='w',encoding='utf-8') as fd:
        header = ['datetime', 'alert_info', 'md5']
        csv_fd = csv.writer(fd)
        csv_fd.writerow(header)
    updateRec(alert_text)
    print(f'First time to save data.No need to compare md5.')
#    exit(keep_kernel=True)  # ipython环境专用命令
    sys.exit()


def updateRec(text):
    '''更新本次查询的alert info to csv file'''
    with open("visaAlert.csv", mode='a+', newline='',encoding='utf-8') as fd:
        p = hashlib.md5()
        p.update(text.encode('utf-8'))
        csv_fd = csv.writer(fd)
        csv_fd.writerow([time.asctime(), text, p.hexdigest()])


def get_text():
    '''get the alert text'''

    url = r'https://www.ustraveldocs.com/cn_zh/index.html?firstTime=No'
    fake_UA = r"Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7"
    req = urllib.request.Request(url, method='GET')
    req.add_header("User-Agent", fake_UA)
    req.add_header("Referer", r"https://www.google.com/search?q=ustraveldocs")

    r = urllib.request.urlopen(req)

    plain_html = r.read().decode()
    soup = BeautifulSoup(plain_html, 'lxml')

    cc = soup.find('div', class_="alert")

    alert = []
    for child in cc.children:
        if isinstance(child, NavigableString):
            continue
        if isinstance(child, Tag):
            alert.append(str(child))

    return "".join(alert)


def compareMD5(text):
    '''比较本次text md5和csv文件最后一次记录的md5值'''
    p = hashlib.md5()
    p.update(text.encode('utf-8'))
    newMD5 = p.hexdigest()

    with open("visaAlert.csv") as fd:
        cfd = csv.DictReader(fd)
        for row in cfd:
            last_md5 = row['md5']

    if newMD5 == last_md5:
        print("No new alert info! Add a record.")
    else:
        print("New alert info happens. Record added.")
        print(f'alert info:\n\n{text}')


def main():
    alert_text = get_text()
    if not os.path.exists("visaAlert.csv"):
        createCSV(alert_text)

    compareMD5(alert_text)
    updateRec(alert_text)  # 无论有没有新alert，都记录下本次alert info md5


if __name__ == "__main__":
    main()
