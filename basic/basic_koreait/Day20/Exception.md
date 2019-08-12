# Exception

```python
"""
1. 예외처리 : 프로그래밍에서 벌어지는 예외적인 상황을 의미한다.
2. 파이썬은 이러한 에러들이 발생하면 프로그램을 중단하고 에러 메세지를 보여준다.
사용법
1. try:
2.    에러상황이 발생할만한 구문
3. except (에러종류) :
4.    에러발생시 실행된다.
"""

num1 = 10
num2 = 0
# 나누기를 0을 사용하면 에러가 난다.(강제종료)
# num3 = num1 / num2 # ZeroDivisionError: division by zero

"""
n = input("정수를 입력하세요 >>> ")
n2 = int(n) # 문자 입력시 강제종료가 된다.
print(n2 + n2)  #  ValueError
"""
"""
try:
    n = input("정수를 입력하세요 >>> ")
    n = int(n)
    print(n)
except ValueError:
    print("문자를 입력했습니다.") 
"""
"""
while True:
    try:
        n = input("정수를 입력하세요 >>> ")
        n = int(n)
        print(10/n)
        if n == -1:
            break
    except Exception:
        print("모든 예외 처리")
    except ValueError:
        print("문자를 입력했습니다.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
"""
"""
while True:
    try:
        n = input("정수를 입력하세요 >>> ")
        n = int(n)
        print(10/n)
        if n == -1:
            break
    except Exception:
        print("모든 예외 처리") # 하나하나 예외처리하기 귀찮을때
"""
lst = [1, 2]
# print(lst[2]) # IndexError: list index out of range
```

