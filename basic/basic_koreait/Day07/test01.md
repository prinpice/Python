# test01

```python
# 주민번호를 입력받고 생일을 출력해보세요
jumin = "880320-1302232"
month = jumin[2:4]
print(month, "월", end="")
day = jumin[4:6]
print(day, "일")
# 주민번호를 입력받고 나이를 출력해보세요 880320-1302232, 010720-3123431
jumin = "880320-1302232" # 18 < age <= 99
age = jumin[0:2]
age = int(age)
if age <= 99 and age > 18: # 2000년생이하
    pass
else:
    print(age)
#=============================================
# 문제 1) 숫자 0~ 10 출력
# 문제 2) 숫자 0 ~ 5, 10 ~ 15 출력
# 문제 3) 숫자 0 ~ 10 중에서 짝수만 출력
# 문제 4) 숫자 0 ~ 10 을 다 더한 합을 출력
#=============================================
# 문제 5) 양수 두개를 입력받고 두 숫자사이의 합을 출력
# 예) 3 , 7 ==> 3 + 4 + 5 + 6 + 7
# 예) 5 , 1 ==> 1 + 2 + 3 + 4 + 5
num1 = int(input("양수1을 입력하세요 >>> "))
num2 = int(input("양수2를 입력하세요 >>> "))
sum = 0
end = 0
while end == 0:
    if num1 > num2:
        sum += num2
        print(num2, "+ ", end="")
        num2 += 1
    elif num1 < num2:
        sum += num1
        print(num1, "+ ", end="")
        num1 += 1
    else:
        sum += num1
        print(num1, "=", sum)
        end = 1

```

