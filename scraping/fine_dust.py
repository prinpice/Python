import requests
from time import sleep
from bs4 import BeautifulSoup as bs
import webbrowser

# 미세먼지
url = "http://www.airkorea.or.kr/index"
res = requests.get(url).text
doc = bs(res, 'html.parser')

result = doc.select_one('.color2').text

print(result[2:])



msg = result




import requests
from time import sleep

# while True:
#     sleep(10)
#     requests.get(url)
requests.get(url)