# test01

```python
# 선택정렬
lst = [10, -9, 5, 19, 9, 1]
# 10 이 나머지 (-9, 5, 19, 9, 1)을 검사해서 가장작은 값이랑 자리를 바꾼다
# 계속 반복
"""
end = 0
while end == 0:
    num2 = 0
    for i in range(len(lst)):
        if lst[i] == 10:
            num1 = i
        if lst[num2] > lst[i]:
            num2 = i
    temp = lst[num1]
    lst[num1] = lst[num2]
    lst[num2] = temp
    print(lst)
"""
# 별찍기
"""
*
**
***
****
****
***
**
*
"""
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print("")
for i in [4, 3, 2, 1]:
    for j in range(i):
        print("*", end="")
    print("")
# 2중리스트
d_list = [[10, 20, 30], [1, 23, -9], [69, 8, -4]]
# 문제 1) 인덱스를 입력받고 해당값출력 (인덱스 2개) (인덱스 012, 012)
# 문제 2) 값을 입력받고 해당 인덱스 출력
# 문제 3) 가장큰값, 인덱스 출력

# 셔플 아래 리스트를 셔플해보세요
shuffle = [0, 1, 2, 3, 4, 5, 6, 7]
```

