import urllib
import requests
from bs4 import BeautifulSoup
# desktop user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
# mobile user-agent
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"
headers = {"user-agent": USER_AGENT}
 
query = "XXX"   # 查询关键
query = query.replace(' ', '+')
URL = f"https://google.com/search?q={query}"  # 谷歌查询网址
resp = requests.get(URL, headers=headers)
 
# 获得查询结果
if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, "html.parser")
    results = []   #网站内容
    page = []   #第一页的页面url
    url = []
    for g in soup.find_all('div', class_='r'):
        anchors = g.find_all('a')
        if anchors:
            link = anchors[0]['href']
            title = g.find('h3').text
            item = {
                "title": title,
                "link": link
            }
            results.append(item)
            url.append(link)
    for a in soup.find_all('tr'):
        for b in a.find_all('a'):
            link = b['href']
            page.append(link)
print(results)
print(page)