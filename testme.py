# -*- coding:UTF-8 -*-
# 下载 tujigu 上面的套图，单进程顺序下载，速度较慢

from urllib import request
from urllib import parse
from urllib import error
from bs4 import BeautifulSoup
import os, sys
from tqdm import tqdm

# make a fake user-agent
headers = {}
headers[
    'User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

# store all page's pic links into pic_links
pic_links = []


def down_pics(title):
    """down all pics in pic_links"""
    name = title.split('/')[0].split()
    name[0], name[1] = name[1], name[0]
    name[-1] = name[-1].replace('写真集', '')
    dirname = "_".join(name)

    try:
        os.mkdir(dirname)
    except FileExistsError:
        import shutil
        shutil.rmtree(dirname, ignore_errors=True)
        os.mkdir(dirname)

    for item in tqdm(pic_links):
        basename = os.path.basename(item)
        localname = os.path.join(dirname, basename)
        try:
            request.urlretrieve(item, localname)
        except error.HTTPError as e:
            print(e.reason)
        except error.URLError as e:
            print(e.reason)
        else:
            print("{} OK".format(item))


def get_plain_html(url):
    '''get URL's html plain text'''
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    respData = response.read()
    htmltext = respData.decode()
    return htmltext, response


def get_next_page_link(bs, response):
    '''get next page's url'''
    content = bs.find('div', id="pages")
    # get all page links
    # print(content.contents)

    # get next page's link
    nextPageLink = content.contents[-1]
    nextPageLink = nextPageLink["href"]
    # print("下一页：{}".format(nextPageLink))

    if nextPageLink == response.geturl():
        print("似乎达了最后一页\n")
        return None
    else:
        return nextPageLink


def save_pics(bs):
    '''save current page's pics in pic_links list'''
    imgs = bs.find("div", class_="content")
    cc = imgs.contents
    # 第一个元素是空值，舍去
    for link in cc[1:]:
        pic_links.append(link['src'])


def _main():
    while True:
        url = input("Input tujigu's URL:  ")
        if parse.urlsplit(url).netloc == 'www.tujigu.com':
            break
        else:
            print("Accept tujigu's url ONLY!!!\nPlease do it again")

    while url:
        plain_html, response = get_plain_html(url)
        bs = BeautifulSoup(plain_html, "lxml")
        save_pics(bs)
        url = get_next_page_link(bs, response)

    title = bs.find('title').string

    # time to download all the pics
    down_pics(title)

    print("\n\nAll Done! {} files are downloaded...".format(len(pic_links)))
    return 0


if __name__ == "__main__":
    sys.exit(_main())
