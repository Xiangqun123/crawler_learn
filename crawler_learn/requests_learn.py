import requests
import re

def demo1():
    # response = requests.get('https://www.hcittech.cn')
    # print(type(response))
    # print(response.status_code)
    # print(type(response.text))
    # print(response.text)
    # print(response.cookies)

    # 声明一个Session对象
    s = requests.Session()
    s.get('https://httpbin.org/cookies/set/number/12345')
    response = s.get('https://httpbin.org/cookies')
    print(response.text)


def demo2():
    content = requests.get("https://book.douban.com").text
    result = re.findall("<li.*?cover.*?href=\"(.*?)\".*?title=\"(.*?)\".*?more-meta.*?author\">(.*?)</span>.*?publisher\">(.*?)</span>", content,re.S)
    print(result)

if __name__ == "__main__":
    # demo1()
    demo2()
