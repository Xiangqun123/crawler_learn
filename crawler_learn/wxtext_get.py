from urllib.parse import urlencode

from lxml.etree import XMLSyntaxError
from requests.exceptions import ConnectionError
from pyquery import PyQuery as pq
import pymongo
import requests
client = pymongo.MongoClient('localhost')
db = client['weixin']
base_url = 'https://weixin.sogou.com/weixin?'
headers = {
    'Cookie': 'SUV=1547815400732876; SMYUV=1547815400733643; UM_distinctid=16860fcb7311cf-0918ca1682eab6-18211c0a-15f900-16860fcb73227b; ABTEST=3|1549556470|v1; IPLOC=CN4111; SUID=E4712C7D642E940A000000005C5C5AF6; SUID=E4712C7D1620940A000000005C5C5AFA; weixinIndexVisited=1; JSESSIONID=aaaGM2UyIgpLjc4stc6Hw; sct=4; PHPSESSID=q02cnip59mkfbvbmts1m0u1426; SNUID=9E673B6A1613964E5BD9D01E171CF301',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1 ',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
}
keyword = '风景'
proxy_pool_url = 'http://127.0.0.1:8080/get'
proxy = None
max_count = 5


def get_proxy():
    try:
        response = requests.get(proxy_pool_url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def get_html(url, count=1):
    global proxy
    print('Crawling', url)
    print('Trying count', count)
    if count >= max_count:
        print('Tried too many counts')
        return None
    try:
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, allow_redirects=False, headers=headers, proxies=proxies)
        else:
            response = requests.get(url, allow_redirects=False, headers=headers)
        if response.status_code == 200:
            return response.text
        if response.status_code == 302:
            # need proxy
            print('302')
            proxy = get_proxy()
            if proxy:
                print('Using proxy', proxy)
                return get_html(url)
            else:
                print('Get proxy failed')
                return None
    except ConnectionError as e:
        print('Error occured', e.args)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


def get_index(keyword, page):
    data = {
        'query': keyword,
        'type': 2,
        'page': page
    }
    queries = urlencode(data)
    url = base_url + queries
    html = get_html(url)
    return html


def parse_index(html):
    doc = pq(html)
    items = doc('.news-box .news-list li .txt-box h3 a').items()
    for item in items:
        yield item.attr('href')


def get_details(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except ConnectionError:
        return None


def parse_details(html):
    try:
        doc = pq(html)
        title = doc('#activity-name').text()
        content = doc('#js_content').text()
        return {
            'title': title,
            'content': content,
        }
    except XMLSyntaxError:
        return None


def save_to_mongo(data):
    if db['articles'].update({'title': data['title']}, {'$set': data}, True):
        print('save to mongo', data['title'])
    else:
        print('save to mongo failed', data['title'])


def main():
    for page in range(1, 101):
        html = get_index(keyword, page)
        # print(html)
        if html:
            article_urls = parse_index(html)
            for article_url in article_urls:
                    article_html = get_details(article_url)
                    if article_html:
                        article_data = parse_details(article_html)
                        print(article_data)
                        if article_data:
                            save_to_mongo(article_data)


if __name__ == "__main__":
    main()

