# for03

```python
"""
$$$$
$$$$
$$$$
"""
for i in range(3): # 세로
    for j in range(4): # 가로
        print("i>>", i, ",", "j>>", j)

# 문제 1) 구구단 출력 2 * 1 = 2 ..... 9 * 9 = 81
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", j*i)
    print("\n")

# 문제 1) 숫자를 입력받고 해당 구구단 출력 ==> 2 ==> 2단 출력
dan = int(input("구구단 : 원하는 단을 입력하세요 >>> "))
for j in range(1, 10):
    print(dan, "*", j, "=", dan*j)
```

