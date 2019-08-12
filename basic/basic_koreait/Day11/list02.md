# list02

```python
# 리스트 함수
# 1. 추가
lst = [1, 2, 3]
lst.append(5)
print(lst) # [1, 2, 3, 5]

# 문제 1) 아래의 리스트의 랜덤값 0 ~ 100까지 5개만 저장해보세요 (함수를 사용)
import random
lst = []
num1 = 0
while num1 < 5:
    lst.append(random.randint(1, 100))
    num1 += 1
print(lst)

# 2. 확장
lst1 = [1, 2, 3]
lst2 = [5, 6, 7]
lst1.extend(lst2)
print(lst1) # [1, 2, 3, 5, 6, 7]

# 3. 삽입 insert (위치, 값)
lst = [1, 2, 3]
lst.insert(0, 10)
print(lst) # [10, 1, 2, 3]

# 4. 삭제 del
del(lst)
# print(lst) # NameError: name 'lst' is not defined
lst = []
print(lst)
lst = [1, 2, 3, 4, 5, 6]
del(lst[0])
print(lst)

# 5. 삭제 remove
lst = [10, 20, 30, 40 , 50]
lst.remove(lst[0])
print(lst)  # [20, 30, 40, 50]

# 6. 정렬 sort
lst = [20, 10, 4, -9]
lst.sort()
print(lst) # 오름차순
# 7. 뒤집기 reverse
lst.reverse()
print(lst1) # [20, 10, 4, -9] 내림차순

# 8. 큰수 작은수 max min
print(max(lst)) # 20
print(min(lst)) # -9
```

