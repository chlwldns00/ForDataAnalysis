import requests
from bs4 import BeautifulSoup

res = requests.get('https://davelee-fun.github.io/blog/crawl_html_css.html')
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.select('tr')  ## select는 find-find_all 처럼 두번연속해서 못쓰는거같다. 하지만 select - find ,  find - select는 사용가능
#data = data[0]
for item in data:
    columns = item.select('td')
    row_str=''
    for column in columns:
        row_str += ''+column
    
    print(row_str)
    