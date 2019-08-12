# while01

```python
# 반복문 ==> while ==> 탈출조건

tree_hit = 0
end = 0
while end == 0:
    tree_hit =tree_hit +1
    print("나무를", tree_hit, "번 찍었다~")
    if tree_hit >= 10:
        print("나무가 넘어간다 ~~")
        end = 1

# 문제 3) 숫자 0 ~ 10 중에서 짝수만 출력
end = 0
num = 0
while end == 0:
    if num % 2 == 0 and num != 0:
        print("짝수 : ", num)
    if num >= 10:
        end =1
    num += 1
# 문제 3) 숫자 0 ~ 10을 다 더한 합 출력 //
total = 0
end = 0
num = 0
while end == 0:
    total = total +num
    if num >= 10:
        end = 1
    num += 1
print("total : ", total)

```

