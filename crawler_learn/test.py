import requests

headers = {
    'Cookie': 'SUV=1547815400732876; SMYUV=1547815400733643; UM_distinctid=16860fcb7311cf-0918ca1682eab6-18211c0a-15f900-16860fcb73227b; ABTEST=3|1549556470|v1; IPLOC=CN4111; SUID=E4712C7D642E940A000000005C5C5AF6; SUID=E4712C7D1620940A000000005C5C5AFA; weixinIndexVisited=1; SNUID=2CB9E5B5C8CD4999F4D779CEC9752154; JSESSIONID=aaaOc0C8pWUnNdLXQ95Hw; sct=2',
    'Host': 'weixin.sogou.com',
    'Upgrade-Insecure-Requests': '1 ',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
}
html = requests.get('https://weixin.sogou.com/weixin?query=风景&type=2&page=1',allow_redirects=False, headers=headers).text
print(html)