# https://ymotongpoo.hatenablog.com/entry/20110108/1294494273

urls = [
 'http://python-history-jp.blogspot.com/', # UTF-8
 'http://iblinux.rios.co.jp/PyJdoc/lib-j/', # EUC-JP
 'http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/encoding.html', # ISO-2022-JP
 'http://www.atmarkit.co.jp/news/200812/04/python.html', # Shift_JIS
 'http://pyunit.sourceforge.net/pyunit_ja.html', # EUC-JP, w/o META
 'http://www.f7.ems.okayama-u.ac.jp/~yan/python/', # ISO-2022-JP, w/o META
 'http://weyk.com/weyk/etc/OpenRPG.html', # Shift_JIS, w/o META
 ]

import gevent
from gevent import monkey
monkey.patch_all() # 諸々の標準ライブラリにパッチを当てる
import urllib
import chardet
from pyquery import PyQuery as pq


def find_hyperlinks(url): # spawnさせたい関数
    data = ''.join(urllib.request.urlopen(url).readlines())
    guess = chardet.detect(data)
    p = dict(url=url,data=data,**guess)
    print('***** %s -> %s (%s)' % (p['url'], p['encoding'], p['confidence']))
    p['data'] = p['data'].decode(p['encoding'])
    d = pq(p['data'])
    page_title = pq(d.find('title')).text()
    
    def extract_hyperlink(page_title, link): # 関数内でさらにspawnさせるために内部で宣言
        link_title = pq(link).text()
        link_url = pq(link).attr.href
        print('(%s) : %s => %s' % (page_title, link_title, link_url))
    jobs = [gevent.spawn(extract_hyperlink, page_title, link) for link in pq(d.find('a'))]
    gevent.joinall(jobs)

        
if __name__ == '__main__':
    jobs = [gevent.spawn(find_hyperlinks, url) for url in urls]
    decoded = gevent.joinall(jobs)