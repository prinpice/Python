# input02

```python
# 캐스팅 ==> int(문자)  ==> int  ==> 정수 ==> 소수점이 없는수 예) -1, 10, 0, 9 ...
# print("10" + "10")  #1010

# print(int("10") + int("10"))   #20

#  print(int("hello"))  #ValueError  ==> 형변환할때는 내용이 숫자여야한다

# test = input()
# print(int(test) +10)
# print("종료")

"""
test = input()
print(int(test) +10)
print("종료")
"""
"""
test = input("숫자를 입력하세요 >>")
print(int(test) + 10)
print("종료")
"""

# 문제 1) 숫자 2개를 입력받고 산술연산을 해보세요 ( + - * / // % )
num1 = input("a를 입력하세요 >>")
num2 = input("b를 입력하세요 >>")
print(int(num1), "+", int(num2), "=", int(num1) + int(num2))
print(int(num1), "-", int(num2), "=", int(num1) - int(num2))
print(int(num1), "*", int(num2), "=", int(num1) * int(num2))
print(int(num1), "/", int(num2), "=", int(num1) / int(num2))
print(int(num1), "//", int(num2), "=", int(num1) // int(num2))
print(int(num1), "%", int(num2), "=", int(num1) % int(num2))
print("종료")


```

