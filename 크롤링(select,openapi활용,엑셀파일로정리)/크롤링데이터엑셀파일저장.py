import requests
from bs4 import BeautifulSoup
import openpyxl

#excel파일 생성
excel_file = openpyxl.Workbook()

#sheet정의
excel_sheet = excel_file.active
excel_sheet.title='크롤링엑셀연습.docx'

#데이터 크롤링해서 리스트저장(한줄한줄)
data_list=[]
for i in range(0,10):
    if i == 0:
        res=requests.get('https://davelee-fun.github.io/')
    else:
        res=requests.get('https://davelee-fun.github.io/page'+str(i+1))
    
    soup=BeautifulSoup(res.content,'html.parser')
    datas=soup.select('div.card h-100') ## ??????????????????? 왜 h-100은 안되고 card는 되나
    for item in datas:
        title=item.select_one('h4.card-text').get_text()
        date=item.select_one('span.post-date').get_text()
        list=[title,date]
        data_list.append(list)
    
    print(i)


#엑셀파일에 데이터 append
for item in data_list:
    excel_sheet.append(item)


#제목, 날짜 길이에 대해 셀 너비 수정
excel_sheet.column_dimensions['A'].width = 100 #100글자
excel_sheet.column_dimensions['B'].width = 20  ## 


#파일 저장
excel_file.save('test.xlsx')

#파일 close (변경사항저장때 필요)
excel_file.close()
        