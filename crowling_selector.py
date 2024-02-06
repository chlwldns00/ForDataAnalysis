import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_test')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('body > h3:nth-child(2)')  

#data = data[0]
for item in data:
    print(item.get_text())
    