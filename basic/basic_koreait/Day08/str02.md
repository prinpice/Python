# str02

```python
atm_data = "김철수 111-111-111 77777 8000"

# 문자열 관련 합수
# 1. 길이(Len)
str1 = "ha ha ha ha ha ha ha ha"
length = str1.__len__()
print(length)
length = len(str1)
print(length)
# 2. 개수 (count)
print("a의 개수", str1.count("a")) # a 의 개수 7
# 3. 인덱스위치 (index)
str1 = "monk@ naver.com"
print("@의 위치 >>>", str1.index("@")) # @의 위치 >>> 4
# 4. 소문자를 대문자로 바꾸기 (upper)
print(str1.upper()) # MONK@NAVER.COM   # AbCd ==> ABCD
# 5. 대문자를 소문자로 바꾸기 (Lower)
print(str1.lower()) # monk@naver.com   # AbCd ==> abcd
"""
# 문제 1) 대문자를 입력하던 소문자를 입력하던 섞어서 입력하던 탈출할 수 있게 만들어보세요
# 예) qUit , QUTI , quit ...
end = ""
while end != "quit":
    end = input("비밀번호를 입력하세요 >>> ")
    end = end.lower() # 대문자를 소문자로 바꿔준다 ==>
print("종료")
"""

# 5. 문자열 바꾸기
str1 = "appletree"
str1 = str1.replace("apple", "lemon")
print(str1) # Lemontree

# 7. 문자열 나누기 (**) dat
str1 = "번호::이름::성적::성별::주소::전화번호"
str1 = str1.split("::")
print(str1) # ['번호', '이름', '성적', '성별', '주소', '전화번호']
atm_data = "김철수 111-111-111 77777 8000"
atm_data = atm_data.split(" ")
print(atm_data) # ['김철수', '111-111-111', '77777', '8000']
print(atm_data[0]) # 김철수
print(atm_data[1]) # 111-111-111
# 문제 1) 이름하고 비밀번호를 입력받고 잔액을 출력하세요
name = input("이름 >>> ")
pw = input("비밀번호 >>> ")
if name == atm_data[0] and pw == atm_data[2]:
    print(atm_data[3], "원")
else:
    print("잘못 입력하셨습니다.")

# 1. 저장 ==> 1. 변수 2. 리스트(배열)
# 2. 찾기 ==> 1. 연산자(4종류) 2. 조건문(if) 3. 반복문(while)
```

