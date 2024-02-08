import requests
from bs4 import BeautifulSoup

url_main='https://davelee-fun.github.io/'
url_about='https://davelee-fun.github.io/about'
res=requests.get(url_main)
soup=BeautifulSoup(res.content,'html.parser')
blog_name=soup.select_one('section.cd-body')
blog_na
for name in blog_name:
    print(name.get_text())


