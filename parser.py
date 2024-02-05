import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D-%EC%A0%84%EC%B2%98%EB%A6%AC-%ED%8C%90%EB%8B%A4%EC%8A%A4-%EC%8B%9C%EA%B0%81%ED%99%94#')
soup = BeautifulSoup(res.content, 'html.parser')

mydata = soup.find('div','clearboth',)
mydata = mydata.find_all('p')
for item in mydata:
    print(item.get_text())
   # print(item.get_image())