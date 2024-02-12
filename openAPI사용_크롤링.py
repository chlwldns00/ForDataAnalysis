import requests
import pprint
import os
import sys
import urllib.request

client_id = 'BTMVavws8Is7jmVpUcSL'
client_secret = 'sDgiapg86l'

# query=urllib.parse.quote('입력할단어') #query검색 입력받는 코드

naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=갤럭시노트10' # +query
header_params = {"X-Naver-Client-Id":client_id, "X-Naver-Client-Secret":client_secret}
res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    data = res.json()
    # pprint.print(data)  형식적 출력
    for index, item in enumerate(data['items']):
        print (index + 1, item['title'], item['link'])
else:
    print ("Error Code:", res.status_code)
    
    