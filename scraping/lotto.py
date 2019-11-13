import random
from bs4 import BeautifulSoup as bs
import requests
import json



# 0. random으로 로또번호를 생성한다.
# 1. 나눔로또 api를 통해 우승 번호를 가져온다.
# 2. random으로 생성된 번호와 우승 번호를 비교해서 나의 등수를 알려준다
# - 1등 : 6개
# - 2등 : 5개 맞고 + 보너스 번호
# - 3등 : 5개
# - 4등 : 4개
# - 5등 : 3개

## json예시

# phonenumber = {
#     "john" : "01012345678",
#     "ashley" : "01098765432"
# }
# phonenumber["john"]

# json_phonenumber = "{\"john\":\"01012345678\", \"ashley\":\"01098765432\"}"
# dict_phonenumber = json.loads(json_phonenumber)
# print(type(dict_phonenumber))

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url).text
dict_json = json.loads(res)
print(type(dict_json))
# doc = bs(dict_json, 'python.parser')
con_num = []
for num in range(1, 7):
    con_num.append(dict_json[f"drwtNo{num}"])
bonusNo = dict_json["bnusNo"]

def pickLotto(): # 함수정의
    my_lotto = sorted(random.sample(range(1, 51), 6))


    matched = len(set(dict_json) & set(my_lotto))


    if matched == 6:
        print("1등입니다.")
    elif matched == 5:
        print("3등 입니다.")
    elif matched == 4:
        print("4등 입니다.")
    elif matched == 3:
        print("5등 입니다.")
    # else:
    #     print("꽝입니다.")

for i in range(100000):
    pickLotto()



print(con_num)

# print(res)

# String 3가지 조작방법
## 1. Concatenation : 글자 합체
name = "john"
loca = "seoul"

"happy" + "hacking"

print("hello " + name + " , this is " + loca + "SSAFY class")

# >>> hello john , this is seoul SSAFY class

## 2. Interpolation : 글자 삽입(수술)


print(f"hello {name}, this is {loca} SSAFY class")

# >>> hello john , this is seoul SSAFY class

# for i in range(1, 7):
#     print(lotto["drwtNo" + str(i)])

# for i in range(1, 7):
#     print(lotto[f"drwtNo{i}"])

## 3. Slicing : 글자 자르기
# greeting = "hello john, this is ashley"
# greeting[x:y]