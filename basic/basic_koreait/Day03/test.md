# test

```python
# 문제 1) 자기소개를 전부 붙여서 출력 해보세요 (자기소개 이름 나이 ...)

print(10, "+", 10, "=", 10+10) # 10 + 10 = 20
# 문제 1)  -(빼기)  +(곱하기)  /(나누기)  를 사용해서 위에처럼 출력해보세요
print(10, "-", 10, "=", 10+10)
print(10, "*", 10, "=", 10+10)
print(10, "/", 10, "=", 10+10, "\n")

print(10, "+", 3, "=", 10+3) # 10 + 3 = 13
# 문제 1) 숫자 자리에 전부 변수를 사용해서 출력 해보세요 - * / // %
num1 = 10
num2 = 3
num3 = num1 + num2

print(num1, "+", num2, "=", num3)
print(num1, "-", num2, "=", num3)
print(num1, "*", num2, "=", num3)
print(num1, "/", num2, "=", num3)
print(num1, "//", num2, "=", num3)
print(num1, "%", num2, "=", num3, "\n")

# 응용문제 1) 아래 길이의 사각형 넓이를 구해보세요   ..  2) 아래길이의 삼각형 넓이를 구해보세요.
width = 20
height = 10
arec = width * height
atri = width * height /2
print("(사각형 넓이) =", arec)
print("(삼각형 넓이) =", atri, "\n")

# 응용문제 2)
second = 100
# 위의 second 를 분초 로 출력해보세요(식을 만들어보세요) 몫 나머지
# 1분 40초
min = second // 60
second1 = second % 60
print(second, "초는", min, "분", second1, "초 이다.\n")

# 심화 ) num4 과 num5 의 값을 교환해보세요 (결과) num4 =30, num5 =20 (변수가 하나 더 필요)
num4 = 20
num5 = 30

num6=num4
num4=num5
num5=num6


print("num4 = ", num4)
print("num5 = ", num5, "\n")


#=======================================================================================================



# 문제 1) 아래 성적의 총합과 평균을 출력해보세요
korScore = 80
engScore = 30
mathScore = 54

sum = korScore + engScore + mathScore
ave = (korScore + engScore + mathScore ) // 3
print("총합은", sum, "점")
print("평균은", ave, "점\n")


# 문제 2) 월급으로 연봉을 구해보세요 (단 세금 10% 제외)
salary = 200

real = salary * 0.9
year = real * 12
print("연봉은", year, "\n")

# 문제 3) 일로 개월 일 을 구해보세요 (단 1개월은 30일로 고정)
day = 200 # 결과 ==> 6개월 20일

month = day // 30
day1 = day % 30
print(day, "일은", month, "개월", day1, "일")



```

