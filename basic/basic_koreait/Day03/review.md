# review01

```python
# 1. 저장 1) 변수 2) 리스트(배열)
# 2. 수정 1) 연산자 4종류  (1. 산술연산자 2. 대입연산자(=) 3. 비교연산자) 2) 조건문(if) 3) 반복문(while)

# 출력 , 입력

# 출력 문제 ) 자기소개
print("자기소개", "이름", "주소")
# 저장 문제 ) 변수
num = 19
print(num)
# 산술연산자 문제 ) 더하기 출력해보세요 10 + 2 = 12
print(10, "+", 3, "=", 10 + 3)
# 변수를 사용해서 산술연산자를 출력해보세요 num1 + num2 = num1 + num2
num1 = 10
num2 = 20
num3 = num1 + num2
print(num1, "+", num2, "=", num3)
# 성적3개를 더해서 합 평균 ==> * /
score1 = 20
score2 = 30
score3 = 40
sum = score1 +score2 +score3
avr = sum/3
print("합 :", sum, ", 평균 :", avr)
# 나머지 ==> 초로 분초 출력  200 // 60, 200% 60
print(200//60, "분", 200%60, "초")
# 입력 ==> 문자로 저장이 딘다 ==> 형변환을 해줘야 숫자로 사용할 수 있다.
num4 = input("숫자를입력하세요 ")
print(int(num4))


# 문제) 성적 3개를 입력받고 총합 평균 출력 하세요
score4 = input("성적1을 입력하세요 >>")
score5 = input("성적2를 입력하세요 >>")
score6 = input("성적3을 입력하세요 >>")
sum1 = int(score4) + int(score5) + int(score6)
ave1 = sum/3
print("총합 :", sum1, "평균", ave1)
print("\n")

# 문제) 초를 입력받고 분초로 출력 하세요
second = input("초를 입력하세요 >>")
min1 = int(second) // 60
second1 = int(second) % 60
print(int(second), "초는", min1, "분", second1, "초 이다.")
print("\n")

# 심화문제) 돈을 입력받고 5만원짜리 1만원짜리 천원짜리가 몇장인지 출력해보세요 단 1000이상으로 입력
# 예 ) 532300  ==> 5만원 10장 만원 3장 천원 2장
money = input("1000원 이상의 돈을 입력하세요 >>")
money1 = int(money) // 50000
money2 = int(money) - (money1 * 50000)
money3 = money2 // 10000
money4 = money2 - (money3 * 10000)
money5 = money4 //1000
print(int(money), "원은 5만원", money1, "장 만원", money3, "장 천원", money5, "장 이다.")
print("\n")
```

