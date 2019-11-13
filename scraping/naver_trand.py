# 1. requests에게 naver.com 요청을 보내서
# 2. 응답받은 문서를 저장하고
# 3. BeautifulSoup 정보를 찾기 좋게 만들고
# 4. 우리가 원하는 정보를 뽑아온다.
# 5. webbrowser를 통해 트랜드 1위 단어를 검색한 페이지를 열어주는 코드

import requests
import bs4
import webbrowser

url= "https://m.comic.naver.com/"

response = requests.get(url)
print(response)
doc = bs4.BeautifulSoup(response.text , 'html.parser') # html문서를 python이 읽기 좋게 만듬
# print(doc)
# result = doc.select_one('.ah_k') # class를 통해서 가져오기 html 문서에 class="ah_k"라고 쓰여있음
# print(result.text)

result = doc.select('.ah_k')

# webbrowser를 통해 result.text에 있는 단어로 검색한 페이지를 연다.
# search_url = "https://search.naver.com/search.naver?query=" + result.text
#  webbrowser.open(search_url)
#  print(type(doc)) #doc의 타입을 알아본다(내용)

for i in result:
    search_url = "https://search.naver.com/search.naver?query=" + i
    webbrowser.open(search_url)