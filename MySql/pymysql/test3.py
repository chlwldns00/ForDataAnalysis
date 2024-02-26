from bs4 import BeautifulSoup
import requests
for page_num in range(10):
    if page_num == 0:
        res = requests.get('https://davelee-fun.github.io/')
    else:
        res = requests.get('https://davelee-fun.github.io/page' + str(page_num + 1))
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('div.card-body')
    for item in data:
        category = item.select_one('a.text-dark').get_text().replace('관련 상품 추천', '').strip()
        product = item.select_one('h4.card-text').get_text().replace('상품명:', '').strip()
        print (category, product)