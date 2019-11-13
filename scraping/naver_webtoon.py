# naver webtoon 화요일 웹툰 긁어오기

import requests
# import bs4
from bs4 import BeautifulSoup as bs
import webbrowser

url = "https://m.comic.naver.com/webtoon/weekday.nhn?week=tue"

res = requests.get(url).text # url의 내용을 text로 긁어온다.
doc = bs(res, 'html.parser') #res에 들어있는 내용이 글자이기 때문에 python을 위해 변형시켜준다.

names = []
imgs = []
result = doc.select('.toon_name')
for i in result:
    names.append(i.text)
    print(i.text)

for e in doc.select('.im_br'):
    imgs.append(e.text)
    print(e.select_one('img')["src"]) #.im_br 클래스 내의 img태그에서 src만 출력


for name in names:
    f = open('./a.txt', 'a+')
    f.write(name+ '\n')
print(len(names))
print(len(imgs))

## 목요일 웹툰
# url = "https://m.comic.naver.com/webtoon/weekday.nhn?week=thu"
# res  = requests.get(url).text
# doc = bs(res, 'html.parser')

# names = ""
# for i in doc.select('.toon_name'):
#     names+= i.text + "\n"
#     print(i.text)