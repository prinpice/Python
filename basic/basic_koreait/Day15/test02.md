# test02

```python
card_shape = ["다이아", "스페이드", "하트", "클로버"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
deck = []
for i in range(4):
    temp = []
    for j in range (10):
        temp.append(card_shape[i])
        temp.append(card_num[j])
        deck.append(temp)
num = 0
for i in deck:
    print(i, end=" ")
    if num % 10 == 9:
        print()
    num += 1
print()
"""
# 문제 1) 셔플
import random
count0, count1, count2, count3 = 0, 0, 0, 0
deck = []
for i in range(40):
    temp = []
    num1 = random.randint(0, 3)
    num2 = random.randint(0, 9)
    temp.append(card_shape[num1])
    if num1 == 0:
        count0 += 1
    elif num1 == 1:
        count1 += 1
    elif num1 == 2:
        count2 += 1
    elif num1 == 3:
        count3 += 1
    temp.append(card_num[num2])
    deck.append(temp)
num = 0
for i in deck:
    print(i, end=" ")
    if num % 10 == 9:
        print()
    num += 1
print()
# 문제 2) 2장씩 나눠주고 게임하기 ==> 2장의 합이 높은 쪽이 승리
# ==================================================================
lst = [10, 6, -7, 200, 5, -9]
# 함수
# 문제 1) 리스트안에 짝수만 출력해주는 함수
def show_lst_even():
    for i in lst:
        if i % 2 == 0:
            print(i)
show_lst_even()
# 문제 2) 리스트안의 짝수의 갯수를 출력해주는 함수
# 문제 3) 리스트 안의 합을 출력해주는 함수
# ==================================================================
# 리스트
# 문제 1) 리스트 안의 합을 출력
# 문제 2) 리스트 안의 짝수만 출력
# 문제 3) 값을 입력받고 인덱스 출력
# 문제 4) 가장 큰 값 출력
```

