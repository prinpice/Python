# operator02

```python
# 논리 연산자 (비교연산자와 함께 사용)
# 1) and  ==> (a == b) and (a == c) 1번 비교도 참이고 2번 비교도 참이면 참
# 2) or   ==> (a == b) or (a == b) 1번 비교가 참이거나 2번 비교가 참이면 참( 둘중 1개만 참이어도 참)
# 3) not  ==> not(a == b)   : 비교가 거짓이면 참

num1 = 10
num2 = 20
num3 = 30
num4 = 40
"""
# 문제 1) 전부 True 가 나오도록 사이사이 값을 변경해보세요
num2 = 10
num3 = 40
print(num1 == num2 and num3 == num4) # False
print(num1 == num2 or num3 == num4) # False
num2 = 20
print(not(num1==num2)) #True
print(num1 != num2 and num3 >= num4) # False
num3 = 50
print(num1 > num2 or num3 > num4) # False
num1 = 20
print(not(num1!=num2)) #False
"""
"""
# 문제 1) 전부 False 가 나오도록 사이사이 값을 변경해보세요
print(num1 == num2 and num3 == num4) # False
print(num1 == num2 or num3 == num4) # False
num2 = 10
print(not(num1==num2)) #True
print(num1 != num2 and num3 >= num4) # False
print(num1 > num2 or num3 > num4) # False
num2 = 20
print(not(num1!=num2)) #False
"""
```

