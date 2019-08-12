# for04

```python
"""
*
**
***
****
"""
"""
****
***
**
*
"""
# 위의 그림을 출력해보세요
# ==> for 로 풀어보세요
for i in range(4):
    for j in range(i+1):
        print("*", end="")
    print("")
for i in [4, 3, 2, 1]:
    for j in range(i):
        print("*", end="")
    print("")
lst = [10, 20, 30, 40, 50, 60]
# 전체 합 평균 출력
total = 0
for i in range(len(lst)):
    total += lst[i]
ave = total / len(lst)
print("전체 합: ", total, "평균: ", ave)
# 35 이상이 숫자의 갯수를 출력
count = 0
for i in range(len(lst)):
    if lst[i] >= 35:
        count += 1
        print(lst[i])
print("35이상: ", count)
# 값을 입력받고 인덱스를 출력
num = int(input("값을 입력하세요 >>> "))
for i in range(len(lst)):
    if num == lst[i]:
        print("인덱스: ", i)
```

