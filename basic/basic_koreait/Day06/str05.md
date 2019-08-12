# str05

```python
# 문자열 슬라이싱 ==> 인덱싱 ==> 범위지정

str1 = "korea it"

print(str1) # korea it

print(str1[1:5])  # orea  ==> 1 <= 범위 < 5
print(str1[5])   # 공백도 변수에 들어갈 수 있다.
print(str1[6])

# 문제 1) ea 만 출력해보자~
print(str1[3:5])

# 주민번호를 입력받고 생일을 출력해보세요
str = input("주민번호를 입력하세요 >>> ")
birth = "생일 : "
birth += str[2:4]
birth += "월"
birth += str[4:6]
birth += "일"
print(birth)
# 주민번호를 입력받고 나이를 출력해보세요 880320-1302232, 010720-3123431
str = input("주민번호를 입력하세요 >>> ")
str1 = int(str[0:2])
print(str1)
print(str)
if str[7] == "1" or str[7] == "2":
    age = 2019-1900-str1
    print("나이: ", age, "세")
elif str[7] == "3" or str[7] == "4":
    age = 2019-2000-str1
    print("나이: ", age, "세")
else:
    print("잘못 입력하셨습니다.")

# 문제 1) 베스킨라빈스 31
# 조건 1) me 는 1~3을 입력받는다 ai 는 랜덤으로 1~3을 저장한다.
# 조건 2) br31 에 me 의 숫자와 ai의 숫자의 합을 누적 저장한다.
# 조건 3) 31을 먼저 넘기는 쪽이 패배
# 예) me = 2 , br = 2 , ai == 3, br = 5 , me == 3 , br ==9 , ai ==1 , br ==9
#미완성
import random
num = random.randint(1, 3)
br = 0
while br > 31:
    if br < 31:
        me = int(input("1~3 사이의 숫자를 입력하세요 >>>"))
        br += me
        print("me : ", me)
        print("br : ", br)
    if br < 31:
        ai = num
        br += ai
        print("ai : ", ai)
        print("br : ", br)

```

