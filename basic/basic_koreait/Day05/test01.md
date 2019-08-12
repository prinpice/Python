# test01

```python
# 출력 ==> 자기소개 (이름, 나이, 주소 한줄로 출력~) (,end="")
print("이름", end="")
print("나이", end="")
print("주소")

# 입력 ==> 숫자 입력, 문자 입력
str1 = input("문자입력")
num = int(input("숫자입력"))
# 자기소개 ==> 입력해서 변수에 저장 후 출력
name =input("이름을 입력하세요 >>> ")
print("이름: ", name)
# 연산자 4종류
num = 10 # 대입연산자(=)

# 1) 숫자 2개를 입력받고 나누기 나머지 몫을 출력 (산술)
num1 = int(input("숫자1를 입력하세요 >>> "))
num2 = int(input("숫자2를 입력하세요 >>> "))
num3 = num1//num2
num4 = num1%num2
print("몫", num3, "나머지:", num4)

# 2) 숫자 1개를 입력받고 60 이상이면 True False 출력(비교)
num = int(input("숫자를 입력하세요 >>> "))
print(num >60)

# 3) 숫자 1개를 입력받고 0보다 작거나 100보다 크면 False 출력(논리)
num = int(input("숫자를 입력하세요 >>> "))
print(0 < num <100)

# 조건문 (if)

# 1) 숫자 1개를 입력받고 "양수""음수""0"출력
num = int(input("숫자를 입력하세요 >>> "))
if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else :
    print("0")

db_id = "koreait"
db_pw = "12345"
# 문제 1) 아이디와 비밀번호를 입력받고 로그인을 해보세요
# 결과 ==> (koreait 님 환영합니다~ 로그인되었습니다 , 아이디 or 비밀번호를 확인해주세요 ) 출력
id = input("아이디를 입력하세요 >>> ")
pw = input("비밀번호를 입력하세요 >>> ")
if db_id == id or db_pw == pw :
    print("koreait 님 환영합니다~ 로그인되었습니다")
else :
    print("아이디 or 비밀번호를 확인해주세요")
```

