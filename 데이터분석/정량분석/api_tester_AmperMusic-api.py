import requests
import json
import googletrans
import webbrowser


## Amper Music API 호출을 위한 URL 및 API 키
url_search = 'https://api.shutterstock.com/v2/audio/search'
url_instruments='https://api.shutterstock.com/v2/audio/instruments'
url_moods='https://api.shutterstock.com/v2/audio/moods'
url_genres='https://api.shutterstock.com/v2/audio/genres'
api_key = 'B8EAqambaqeUVFCpHLU8V1c9rKZan3Zr'


##악기 장르 분위기 예시를 호출하는 API코드

#response = requests.get(url_(example),headers=headers,params={})

## Amper Music API(url_search)에 전송할 데이터

duration_from=100  
duration_to=180
#bpm=80~160
bpm_from=int(input("bpm_from:"))
bpm_to =int(input("bpm_to:"))
moods_str=input("감정입력(하나입력후 띄어쓰기):")
moods=moods_str.split(' ')
instruments_str=input("악기입력(하나입력후 띄어쓰기):")
instruments=instruments_str.split(' ')
genre_str=input("장르입력(하나입력후 띄어쓰기):")
genre=genre_str.split(' ')


## Amper Music API 호출
pos=0
music_list=1
for i in range(1,10):
    response = requests.get(url_search, headers={'Authorization': 'Bearer v2/QXN1UWtHM0pRbGRweG9SS2RKbVBPMVhRM3l6T0s5T0cvMzg4OTk0Nzg3L2N1c3RvbWVyLzQveFZKTDFfTC1aY0Jwc2Ywb3N1WnBDUHk5Znl1c280RVNscXRqZ05KTEQwM2VaOHUxcDh0NFR2aU5mM01nNnYxWXRLVHNVamQzZXZOOXpPLWIxX2JZWWlVbHVIZ1d1M1FoTmZHQWR5Z2JfNzB2ZkhnNm1jbGk5eENXZzlkRGE3X0ZmQWVfVTRSSlcwOC13dll2Ri05ajJKVDgxZ1FPelA5RVktSUxPQi1XOUFKRlZtcERLMUhWX3d6eG9kSjJXWHRNRFktVHNZeHQ4ZmE1QUs3ZVRzUlExQS9Jek9la3Q4ZmZvMUxFMGJPSnZrbzBR'}, 
    params={"page":i,"per_page":40,"genre":genre,"instruments":instruments,"moods":moods,"bpm_from":bpm_from,"bpm_to":bpm_from,"duration_from":duration_from,"duration_to":duration_to})
    
    if response.status_code!=200:
        print("서버오류입니다 다시시도해주세요.")
        print(f"Error searching audio: {response.status_code} - {response.text}")
    
    else:
        results = response.json()['data']
        #print(results)
        pg=response.json()['page'] # 음악 라이브러리의 몇번째 페이지를 탐색하고 있는지 출력
        print(pg)
        print("탐색중입니다.....")

        if results and pos==0:  #만약 검색했을때 데이터가 존재한다면
            for result in results:
                    print(music_list,"번째 음악입니다")            #음악정보들 출력
                    print(result['id'])
                    idd=result['id']                               #세부정보 출력을 위한 id파싱
                    print(result['description'])
                    translator=googletrans.Translator()
                    tex=translator.translate(text, dest='en',src='ko') #음악 묘사 정보를 한글로 번역해서 출력
                    print(tex.text)
                    print(result['assets']['preview_mp3']['url']) #url정보 출력
                    webbrowser.open(u) #url 바로 웹사이트에서 열기
                    
                    info_url ='https://api.shutterstock.com/v2/audio/'+idd+'?view=full&search_id=00000000-0000-0000-0000-000000000000'
                    response = requests.get(info_url, headers={'Authorization': 'Bearer v2/QXN1UWtHM0pRbGRweG9SS2RKbVBPMVhRM3l6T0s5T0cvMzg4OTk0Nzg3L2N1c3RvbWVyLzQveFZKTDFfTC1aY0Jwc2Ywb3N1WnBDUHk5Znl1c280RVNscXRqZ05KTEQwM2VaOHUxcDh0NFR2aU5mM01nNnYxWXRLVHNVamQzZXZOOXpPLWIxX2JZWWlVbHVIZ1d1M1FoTmZHQWR5Z2JfNzB2ZkhnNm1jbGk5eENXZzlkRGE3X0ZmQWVfVTRSSlcwOC13dll2Ri05ajJKVDgxZ1FPelA5RVktSUxPQi1XOUFKRlZtcERLMUhWX3d6eG9kSjJXWHRNRFktVHNZeHQ4ZmE1QUs3ZVRzUlExQS9Jek9la3Q4ZmZvMUxFMGJPSnZrbzBR'}, 
                                params={"id":idd})
                    results_genre = response.json()['genres']
                    results_inst=response.json()['instruments']
                    results_moods=response.json()['moods']
                    bpm=response.json()['bpm']
                    print(results_genre)
                    print(results_inst)
                    print(results_moods)
                    print(bpm)
                    
                    music_list+=1              #총 4개를 출력해야하기 위해 검색된 노래가 4개가 넘어가면 종료
                    if music_list==5:
                        print("탐색끝")
                        break


    

 


if music_list==1: #조건에 맞는 음악을 응답받지 못하였을때   
    print("조건에 맞는 음악을 생성하지 못하엿습니다 다시 입력해주세요:")
   

