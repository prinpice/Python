# for

```python
# 보조 제어문 break, continue (점프문)

# 1. break ==> 반복문을 즉시 빠져나간다.
# 2. continue ==> 반복문의 조건으로 즉시 올라간다(아래 내용을 무시함)
for i in range(10):
    if i > 5:
        break
    print(i, end="") # 012345 ==> 조건에 의해서 break 가 실행되어 반복문 종료
print()
for i in range(10):
    if i < 5:
        continue
    print(i, end="") # 56789
    # ==> 조건에 의해서 continue 가 실행되어 아래실행문을 무시하고 조건문으로 점프
```

