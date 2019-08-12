# test02

```python
st = [10, 20, 30 ,40, 50, 60]
# 전체 합 평균 출력
# 35 이상인 숫자의 갯수를 출력
# 값을 입력 받고 인덱스를 출력
# 구구단 출력
# ==============================================
"""
****
***
**
*
"""
APT = [[101, 102, 103, 104]
       ,[201, 202, 203, 204]
       ,[301, 302, 303, 304]]
"""
# 문제 1) 전체 합 평균
total = 0
for i in range(len(APT)):
    for j in range(len(APT[i])):
        total += APT[i][j]
print("전체 합: ", total)
"""
"""
# 문제 2) 각층별 합
for i in range(len(APT)):
    total = 0
    for j in range(len(APT[i])):
        total += APT[i][j]
    print(i+1, "층 합: ", total)
"""
"""
# 문제 3) 동을 입력받고 인덱스 출력 202 ==> 0, 1
dong = int(input("동을 입력하세요 >>> "))
for i in range(len(APT)):
    for j in range(len(APT[i])):
        if dong == APT[i][j]:
            print(i, ",", j)
"""
"""
# 문제 4) 인덱스를 입력받고 동출력
index1 = int(input("인덱스1을 입력하세요 >>> "))
index2 = int(input("인덱스2를 입력하세요 >>> "))
for i in range(len(APT)):
    for j in range(len(APT[i])):
        if index1 == i and index2 == j:
            print(APT[i][j])
"""
"""
# 문제 5) 동 2개를 입력받고 서로 교환
dong1 = int(input("동1을 입력하세요 >>> "))
dong2 = int(input("동2를 입력하세요 >>> "))
temp_dong = 0
i1, i2, j1, j2 = 0, 0, 0, 0
for i in range(len(APT)):
    for j in range(len(APT[i])):
        if dong1 == APT[i][j]:
            i1 = i
            j1 = j
        elif dong2 == APT[i][j]:
            i2 = i
            j2 = j
temp_dong = APT[i1][j1]
APT[i1][j1] = APT[i2][j2]
APT[i2][j2] = temp_dong
print(APT)
"""
PAY = [[10000, 20019, 32212, 21830],
       [20000, 20119, 37712, 71230],
       [30000, 45019, 38712, 67230]]
# 문제 1) PAY 에 [[], [], []] 모양으로 랜덤값 저장 10000 ~ 50000 (선택)
PAY = []
import random
for i in range(3):
    pay = []
    for j in range(4):
        pay.append(random.randint(10000, 50000))
    PAY.append(pay)
print(PAY)
"""
# 문제 2) 동을 입력받고 관리비 출력, 관리비 입력받고 동출력
dong = int(input("동을 입력하세요 >>> "))
for i in range(len(APT)):
    for j in range(len(APT[i])):
        if dong == APT[i][j]:
            print("관리비: ", PAY[i][j])
dong_pay = int(input("관리비를 입력하세요 >>> "))
for i in range(len(PAY)):
    for j in range(len(PAY[i])):
        if dong_pay == PAY[i][j]:
            print("동: ", APT[i][j])
"""
"""
# 문제 3) 가장 관리비 많이 나온집 출력
max1 = max(PAY[0])
for i in range(len(PAY)):
    if max1 < max(PAY[i]):
        max1 = max(PAY[i])
for j in range(len(PAY)):
    for k in range(len(PAY[j])):
        if max1 == PAY[j][k]:
            print("동: ", APT[j][k])
"""
"""
# 문제 4) 각 층별 관리비 합 출력
for i in range(len(PAY)):
    total = 0
    for j in range(len(PAY[i])):
        total += PAY[i][j]
    print(i+1, "층 관리비 합: ", total)
"""
"""
# 문제 5) 동 2개를 입력받고 관리비 교환
dong1 = int(input("동1을 입력하세요 >>> "))
dong2 = int(input("동2를 입력하세요 >>> "))
i1, i2, j1, j2, temp_pay = 0, 0, 0, 0, 0
for i in range(len(APT)):
    for j in range(len(APT[i])):
        if dong1 == APT[i][j]:
            i1 = i
            j1 = j
        elif dong2 == APT[i][j]:
            i2 = i
            j2 = j
temp_pay = PAY[i1][j1]
PAY[i1][j1] = PAY[i2][j2]
PAY[i2][j2] = temp_pay
print(PAY)
"""
```

