
import requests
from bs4 import BeautifulSoup
import re
import pymysql
db = pymysql.connect(
    host='localhost', # 127.0.0.1 , 0.0.0.0 
    port=3306, 
    user='root', # root
    passwd='ryan1024@', 
    db='mydata', 
    charset='utf8')
cursor=db.cursor()
pg=0
res = requests.get('https://davelee-fun.github.io/') #웹사이트 get request 1페이지
soup = BeautifulSoup(res.content, 'html.parser') #html 파싱
items = soup.select('div.card h')
product_id=17890001
page_num=pg+1
for item in items:
        
    recom_info=item.select_one('a.text-dark')
    product_name=item.select_one('h4.card-text')
    provider=item.select_one('a[target="_blank"]')
    register_date=item.select_one('span.post-date')
    SQL=recom_info
    print(SQL)
        #cursor.execute(SQL)