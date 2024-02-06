import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('body > h3:nth-child(2)')  ## select는 find-find_all 처럼 두번연속해서 못쓰는거같다. 하지만 select - find ,  find - select는 사용가능
#data = data[0]
for item in data:
    print(item.get_text())
    