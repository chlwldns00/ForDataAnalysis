# 데이터 분석가를 위한 역량 기르기
---
## 목차
1. [데이터 수집 - 데이터 크롤링, 전처리, 엑셀파일자동화](#1데이터-수집---데이터-크롤링-전처리-엑셀파일자동화)
2. [데이터 저장(mysql, nosql)](#2데이터-저장mysql-nosql)
   - [MYSQL](#mysql)
   - [NoSQL(MongoDB)](#nosqlmongodb)
3. [파이썬 데이터 분석](#4파이썬-데이터-분석)
   - [Pandas, Numpy 활용 데이터 분석 프로젝트](#pandas-numpy-이용-데이터-분석-프로젝트weit-데이터스테이션)
4. [머신러닝 알고리즘 학습](#5머신러닝-알고리즘-학습)

5. [자격증](#자격증)
---  
## 1.데이터 수집 - 데이터 크롤링, 전처리, 엑셀파일자동화  
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
- *[크롤링+엑셀자동화 프로젝트](https://github.com/chlwldns00/ForDataAnalysis/blob/main/%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81%2B%EB%AC%B8%EC%84%9C%EC%9E%90%EB%8F%99%ED%99%94(%EC%97%91%EC%85%80)/%EC%8B%A4%EC%8A%B5/%EC%B5%9C%EC%A2%85_%EC%98%88%EC%A0%9C%EC%82%AC%EC%9D%B4%ED%8A%B8_%ED%81%AC%EB%A1%A4%EB%A7%81%2B%EC%A0%84%EC%B2%98%EB%A6%AC%2B%EC%97%91%EC%85%80%EC%A0%80%EC%9E%A51.ipynb)*    
1.웹사이트 크롤링    
2.크롤링데이터 엑셀파일화

[🔝 목차로 돌아가기](#목차)
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
- *[파이썬환경에서 mysql연동 사용 실습](https://github.com/chlwldns00/ForDataAnalysis/blob/main/MySql/pymysql/pymysql%EC%8B%A4%EC%8A%B5%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8.ipynb)*       
1.pymysql 라이브러리로 mysql DB table연동  
2.bs4라이브러리로 웹페이지 크롤링  
3.[크롤링한 데이터로 table채우기 및 검색연산](https://github.com/chlwldns00/ForDataAnalysis/blob/main/MySql/sakilaDB/sakila-db%EC%8B%A4%EB%AC%B4%EC%8B%A4%EC%8A%B5/GMARKET_db%EC%97%90%EC%84%9C%20%EC%8B%A4%EB%AC%B4%EC%88%98%ED%96%89%EC%8B%A4%EC%8A%B5.sql)      
### NoSQL(MongoDB)  
- MongoDB 데이터베이스 구조 이해  
  1.how to install  
  2.클라우드(aws,google,ncp등)에서 돌리는 방법(linux ubuntu사용)  
- MongoDB CRUD 문법 [mflix 빅데이터베이스 이용](https://github.com/chlwldns00/ForDataAnalysis/tree/main/nosql/sampleDB/sample_mflix)   
  1.실제 mongoDB 생성후 실습
- 파이프라인을 이용한 aggregation 문법이해  [mflix 빅데이터베이스 이용]   
  1.sharding이용    
  2.크게 match,group,count,sort,unwind,limit : {}안에서 세부조건 덧붙이기    
  3.[aggregation을 활용한 검색 실습](https://github.com/chlwldns00/ForDataAnalysis/blob/main/nosql/Aggregation/mongoDB_Aggregation%EC%8B%A4%EB%AC%B4%EC%8B%A4%EC%8A%B5.js)  
- pymongo라이브러리를 이용하여 파이썬환경에서 mongoDB연동해 사용하기  
  1.pymongo로 python <-> mongoDB 연동    
  2.pymongo 로 mongoDB CRUD 나타내기    
  3.pymongo 로 aggregation문법 사용하기  
- *[PYMONGO 활용 프로젝트](https://github.com/chlwldns00/ForDataAnalysis/blob/main/nosql/Pymongo/PYMONGO_%EC%8B%A4%EB%AC%B4%EC%8B%A4%EC%8A%B5.ipynb)*    
  1.pymongo 라이브러리로 mongoDB collection 연동    
  2.bs4라이브러리로 웹페이지 크롤링    
  3.크롤링한 데이터로 collection 채우기 및 검색연산  

  [🔝 목차로 돌아가기](#목차)
  ------------
## 3.파이썬 데이터 분석
  ## pandas,numpy 이용 데이터 분석 프로젝트(WEIT 데이터스테이션)  
  > 데이터 스테이션 수료([데이터 분석 팀프로젝트 공동 레포지토리](https://github.com/chlwldns00/weit) ) 
  > 실무 문제상황 데이터분석 프로젝트 수료([수료증 링크](https://drive.google.com/file/d/1pT-QhDk535N29j10yS7d5qHavlPuxF8c/view?usp=drive_link))
      
  > 실제 사용되는 데이터를 가지고 데이터 EDA진행 및 분석보고서 작성    
- [복지패널 데이터 분석 프로젝트](https://github.com/chlwldns00/ForDataAnalysis/blob/main/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D/%EB%B3%B5%EC%A7%80%ED%8C%A8%EB%84%90%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D.ipynb)  
   - 복지를 위한 시민정보 데이터를 분석하고, 연령대,성별,종교,이혼율 에 대한 EDA분석 진행  
- [지역화폐 데이터 분석 프로젝트](https://github.com/chlwldns00/project_weit)  
   - 지역화폐 데이터를 분석하고, 지역화폐를 활성시키기 위한 솔루션 도출


   [🔝 목차로 돌아가기](#목차)
---------------
## 4.머신러닝 알고리즘 학습
> sklearn으로 머신러닝의 주요 알고리즘 학습
   - [사이킷런 모듈학습](https://github.com/chlwldns00/ScikitLearn_Practice/tree/main/%EC%82%AC%EC%9D%B4%ED%82%B7%EB%9F%B0%20%EB%AA%A8%EB%93%88%20%ED%95%99%EC%8A%B5)
   - [분류알고리즘](https://github.com/chlwldns00/ScikitLearn_Practice/tree/main/%EB%B6%84%EB%A5%98%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
   - [회귀알고리즘](https://github.com/chlwldns00/ScikitLearn_Practice/tree/main/%ED%9A%8C%EA%B7%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)
   - [텍스트마이닝](https://github.com/chlwldns00/ScikitLearn_Practice/tree/main/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EB%A7%88%EC%9D%B4%EB%8B%9D)
> Kaggle데이터로 [실습 진행](https://github.com/chlwldns00/scikitlearn-)
 [🔝 목차로 돌아가기](#목차)
--------------


## 자격증
- 토익스피킹 IH(2024년 1월 합격)
- 데이터분석준전문가(2023년 1차시험 최종 합격)
- 빅데이터분석기사(2023년 2차시헙 필기합격)
- 정보처리기사(필기 2023년 3차 필기 합격)

  [🔝 목차로 돌아가기](#목차)

---
