# if

```python
# 조건문(if)
"""
1. if ==> 키워드
2. num1 == num2 : ==> 조건 ==> 조건이 사실이면 실행문이 실행된다 (거짓이면 무시)
3. 공백4칸 ==> 실행문 ==> 공백뒤에 적은내용은 if 문의 조건이 참일경우만 작용된다.
4. else : ==> 조건이 거짓이면 실행된다.
"""
"""
num1 = 10
num2 = 20

if num1 == num2:
    print("서로 같다")  # 4칸을 띄어야된다 (space 4번)
else :
    print("서로 다르다")
"""
"""
num1 = 20
num2 = 20

if num1 == num2:
    print("서로 같다")  # 4칸을 띄어야된다 (space 4번)
else :
    print("서로 다르다")
"""
"""
# 문제 1) 숫자(0~100) 하나를 입력받고 60이상이면 "합격" 미만이면 "불합격" 출력해보세요.
score1 = input("점수를 입력하세요>>>")
print(int(score1))

if int(score1) >= 60:
    print("합격")
else :
    print("불합격")
"""
"""
# 문제 2) 성적 3개를 입력받고 평균이 60 이상이면 합격 미만이면 불합격
score1 = input("성적1을 입력하세요>>>")
score2 = input("성적2를 입력하세요>>>")
score3 = input("성적3을 입력하세요>>>")

ave = (int(score1) + int(score2) + int(score3))/3
print("평균:", ave)
if ave >= 60:
    print("합격")
else :
    print("불합격")
"""
"""
score1 = int(input("숫자1을 입력하세요 >>> "))
score2 = int(input("숫자2를 입력하세요 >>> "))
score3 = int(input("숫자3을 입력하세요 >>> "))
total = score1 + score2 + score3
avr = total / 3
if avr >= 60:
    print("합격")
else: 
    print("불합격")
"""
"""
# 문제 3) 숫자 하나를 입력받고 양수인지 음수인지 0인지 출력
num = input("숫자를 입력하세요>>>")

if int(num) > 0:
    print("양수")
elif int(num) <0:
    print("음수")
else :
    print("0")
"""
"""
num1 = int(input("숫자를 입력하세요 >>> "))
if num1 > 0:
    print("양수")
if num1 < 0:
    print("음수")
if num1 == 0:
    print("0")
"""
"""
# 문제 4) 숫자 하나를 입력받고 짝수인지 홀수인지 출력 ( 힌트 : 나머지)
num = input("숫자를 입력하세요>>>")

num1 = int(num) % 2

if num1 == 1:
    print("홀수")
else :
    print("짝수")
"""
"""
num2 = int(input("짝수홀수를 입력하세요"))
# 어떤수를 입력하든 2로 나누면 나머지는 0 or 1이 나온다.
if num2 % 2 ==0:  # 10 % 2 ==> 0 , 9 % 2 ==> 1 , 10000000 % 2 ==> 0 
    print("짝수")
else:
    print("홀수")
"""
"""
# 문제 5) 숫자 2개를 입력받고 ?? 가 ??보다 크다 작다 같다 출력
num1 = input("숫자1을 입력하세요>>>")
num2 = input("숫자2를 입력하세요>>>")

if int(num1) > int(num2):
    print(int(num1), "가", int(num2), "보다 크다")
elif int(num1) < int(num2):
    print(int(num1), "가", int(num2), "보다 작다")
else :
    print(int(num1), "와", int(num2), "가 같다")
"""
```

