import json
import appdirs
import requests




# API 엔드포인트 URL
url = "https://localpay-806adcefc827.herokuapp.com/summaries.json"


# GET 요청 보내기
response = requests.get(url,params={'page':1})

# 응답 상태 코드 확인
if response.status_code == 200:
    # JSON 데이터 출력

    json_data = response.json()
    print(json_data)
else:
    print(f"Failed to retrieve data: {response.status_code}")
