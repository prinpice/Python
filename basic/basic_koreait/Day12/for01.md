# for01

```python
# for 문
# while 보다 조금 간단하게 사용가능하다
# 1. for ==> 키워드
# 2. 임시변수 in 리스트 ==> 리스트의 값을 하나씩 변수에 저장한다.

print(range(5)) # range(0, 5) ==> 0 ~ 4 까지 저장되어 있는 리스트

for i in range(5):
    print(i, end="") # 01234
print()
print("=================================")
for i in range(1, 15):
    print(i, end="") # 1234567891011121314
print()
print("=================================")
for i in [10, 30, 1, -1, 30, 345, 42]:
    print(i, end="") # 10301-13034542
print("\n")
lst = []
# 문제 1) for 문을 사용해서 리스트에 랜덤값 0 ~ 100 을 5개 저장해보세요
import random
for i in range(5):
    lst.append(random.randint(0, 100))
print(lst)
# 문제 2) 랜덤값 중에서 성적이 60 이상만 출력
for i in range(5):
    if lst[i] >= 60:
        print("합격 >>> ", lst[i])

for i in ["철수", "영수", "영희"]:
    print(i)
```

