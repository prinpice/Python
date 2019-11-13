# Bithumb에서 코인 이름 + 가격 긁어오기

import requests
from bs4 import BeautifulSoup as bs

url = "https://www.bithumb.com/"
res = requests.get(url).text
doc = bs(res, 'html.parser')
# res = doc.select('.coin_list')

# for coin in res:
#     print(coin.select_one('strong').text)

# for coin in res:
#     print(coin.select('strong'))

res = doc.select_one('tr.one:nth-child(1) > td:nth-child(1) > p:nth-child(2) > a:nth-child(1) > strong:nth-child(1)')
print(res)