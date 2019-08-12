# test

```python
db_id = "koreait"
db_pw = "12345"
# 문제 1) 아이디와 비밀번호를 입력받고 로그인을 해보세요
# 결과 ===> (koreait 님 환영합니다~ 로그인되었습니다 , 아이디 or 비밀번호를 확인해주세요) 출력

# 연산자 4종류
num = 10 # 대입연산자(=)
# 1) 숫자 2개를 입력받고 나누기 나머지 몫을 출력 (산술)
# 2) 숫자 1개를 입력받고 60 이상이면 True False 출력 (비교)
# 3) 숫자 1개를 입력받고 0보다 작거나 100보다 크면 False 출력 (논리)
num = int(input("숫자를 입력하세요 >>> "))
print(num > 100 or num<0)

# 조건문 (if)
# 1) 숫자 1개를 입력받고 "양수""음수""0" 출력
num = int(input("숫자를 입력하시오 >>> "))
if num <0:
    print("음수")
elif num>0:
    print("양수")
else:
    print("0")
# 2) 숫자 2개를 입력받고 "크다""작다""같다"를 출력
num1 = int(input("숫자1을 입력하시오 >>> "))
num2 = int(input("숫자2를 입력하시오 >>> "))
if num1 > num2:
    print("크다")
elif num1 < num2:
    print("작다")
else:
    print("같다")

# while
# 문제 1) 숫자 0 ~ 10 출력
num = 0
while num <=10:
    print(num)
    num += 1
print("\n")
# 문제 2) 숫자 0 ~ 5 , 10~ 15 출력
num = 0
while num <=15:
    if num <=5 or num >=10:
        print(num)
    num += 1
print("\n")
# 문제 3) 숫자 0 ~ 10 중에서 짝수만 출력
num = 0
while num <=10:
    if num % 2 == 0:
        print(num)
    num +=1
print("\n")
# 문제 4) 숫자 0 ~ 10 을 다 더한 합 출력
num = 0
sum = 0
while num <=10:
    sum = sum + num
    print(sum)
    num +=1
print("\n")
# 문제 5) 숫자 0 ~ 100중에서 3의 배수이면서 5의 배수만 출력
num = 0
while num<=100:
    if num % 3 == 0 and num % 5 == 0:
        print(num)
    num +=1

```

