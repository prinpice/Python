# list01

```python
list1 = []  # 빈리스트 생성
print(list1) #[]

list1 = ["c", 1, 2]

print(list1) # ['c', , 2]

list1 = [[10,20, 30, 100], [40, 50, 60, 120], [70, 80, 90, 130]] # [[1,2, 3], [4, 5, 6], [7, 8, 9]]
print(list1)
print(list1[0]) # [1, 2, 3]
print(list1[0][0]) # 1
print(list1[1][2]) # 6
print("===============================================")
num1 = 0
while num1 < 3:
    num2 = 0
    while num2 < 4:
        print(list1[num1][num2], " ", end="")
        num2 += 1
    print("\n")
    num1 += 1
# 문제 1) 인덱스를 입력받고 값 출력 ==> 인덱스 2개
# 1번 인덱스 ==> 세로
# 2번 인덱스 ==> 가로

# 문제 2) 값을 입력받고 인덱스 출력 ==> 인덱스 2개

# 전체 합출력
num1 = 0
total = 0
while num1 < 3:
    num2 = 0
    while num2 < 4:
        total += int(list1[num1][num2])
        num2 += 1
    num1 += 1
print("전체 합: ", total)

# 각 리스트 합출력
total1 = 0
total2 = 0
total3 = 0
num1 = 0
while num1 < 3:
    num2 = 0
    if num1 == 0:
        while num2 < 4:
            total1 += int(list1[num1][num2])
            num2 += 1
    elif num1 == 1:
        while num2 < 4:
            total2 += int(list1[num1][num2])
            num2 += 1
    elif num1 == 2:
        while num2 < 4:
            total3 += int(list1[num1][num2])
    num1 += 1
print("list1의 합: ", total1)
print("list2의 합: ", total2)
print("list3의 합: ", total3)
```

