# test01

```python

# 문제 1) 아래 리스트를 셔플해보세요~
# 방법 1) 랜덤으로 인덱스를 뽑아서 인덱스 0의 값이랑 교환 100번
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
import random
num = 0
temp = 0
while num < 100:
    num1 = random.randint(0, 9)
    temp = lst[num1]
    lst[num1] = lst[0]
    lst[0] = temp
    print(lst)
    num += 1

"""
# 문제 2) 아래와 같이 출력해보세요
num = 0
while num < 20:
    if num % 5 != 4:
        print("$", end="")
    else:
        print("$")
    num += 1
"""
"""
$$$$$
$$$$$
$$$$$
$$$$$
"""
# 리스트문제 1) 아래 리스트의 총합 평균 출력~
# 인덱스를 입력받고 값 출력
# 값을 입력받고 인덱스를 출력해보세요~~
lst = [10, 20, -1, 40, 200, 6]
"""
num = 0
total = 0
while num < len(lst):
    total += lst[num]
    num += 1
ave = total / len(lst)
print("총합: ", total, "평균: ", ave)
"""
"""
index = int(input("인덱스를 입력하세요 >>> "))
print(lst[index])
"""
"""
num = int(input("값을 입력하세요 >>> "))
num1 = 0
while num1 < len(lst):
    if num == lst[num1]:
        print(num1)
    num1 += 1
"""
```

