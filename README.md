# 데이터 분석가를 위한 역량 기르기 '*표시는 여러번보자'

## 1.데이터 수집 - 데이터 크롤링 , 전처리, 엑셀파일자동화 (정적 웹 페이지 데이터(html,css), openAPI데이터(JSON,XML)) 활용  
- How to 크롤링  
1.크롤링에 활용되는 BeautifulSoap 라이브러리 학습  
2.웹 서버에서 어떻게 웹문서를 주고받는지 (HTTP Requests)  
- HTML/CSS 정적 웹문서 크롤링  
1.find와 select 의 활용  
- 엑셀파일자동화  
1.크롤링후 엑셀파일 생성, 크롤링한 데이터 저장, 파일 save  
2.openpyxl라이브러리 학습    
- openAPI의 데이터를 활용한 크롤링    
1.openAPI 사용 셋팅 코드 + JSON데이터 활용 크롤링(네이버 openAPI활용 데이터 사용)  
2.XML데이터 활용 크롤링(정부 공공데이터 openAPI 활용 데이터 사용)
- *크롤링+엑셀자동화 프로젝트*    
1.웹사이트 크롤링    
2.크롤링데이터 엑셀파일화    
--------

## 2.데이터 저장(mysql, nosql)  
### MYSQL  
- 데이터베이스와 RDBMS 이해
- SQL문법  
1.데이터베이스 스키마 구상  
2.데이터베이스 테이블 설정  
3.sql문으로 데이터 입력/수정/삭제/검색  
4.무결성원칙  
- 실제DB로 SQL실무 실습  
1.여러가지 조건문 수행  
2.테이블 JOIN, INDEX 작업
- *DB CRUD 프로젝트*    
1.pymysql 라이브러리로 mysql DB table연동  
2.bs4라이브러리로 웹페이지 크롤링  
3.크롤링한 데이터로 table채우기 및 검색연산      
### NoSQL(MongoDB)  
- MongoDB 데이터베이스 구조 이해  
  1.how to install  
  2.클라우드(aws,google,ncp등)에서 돌리는 방법(linux ubuntu사용)  
- MongoDB CRUD 문법 [mflix 빅데이터베이스 이용]   
  1.실제 mongoDB 생성후 실습
- 파이프라인을 이용한 aggregation 문법이해  [mflix 빅데이터베이스 이용]   
  1.sharding이용    
  2.크게 match,group,count,sort,unwind,limit : {}안에서 세부조건 덧붙이기    
  3.aggregation을 활용한 검색 실습(***)  
- pymongo라이브러리를 이용하여 파이썬환경에서 mongoDB연동해 사용하기  
  1.pymongo로 python <-> mongoDB 연동    
  2.pymongo 로 mongoDB CRUD 나타내기    
  3.pymongo 로 aggregation문법 사용하기  
- *PYMONGO 활용 프로젝트*    
  1.pymongo 라이브러리로 mongoDB collection 연동    
  2.bs4라이브러리로 웹페이지 크롤링    
  3.크롤링한 데이터로 collection 채우기 및 검색연산  

  ------------
  ## 3.python벡엔드,서버기술 및 파이썬 어플리케이션 개발  
  ### Flask
  - Flask, 벡엔드 기본구조  
   1.벡엔드 개발 기본구조 이해    
   2.flask 프레임워크 기본구조 이해  
   3.flask 문법이해  
   

