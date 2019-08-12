# list01

```python
# 리스트 연산자
# *
lst = [0] * 5
print(lst)
lst = ["안녕"] * 3
print(lst)
lst = ["안녕", 0] * 3
print(lst)
# +
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst1 + lst2)
# = 대입연산자(수정)
lst = [1, 2, 3]
lst[1] = 100
print(lst) # [1, 100, 3]
# 리스트 초기화
lst = []
print(lst) # []

lst = [1, 2, 3, 4, 5, 7]
lst[1:2] = [100, 100, 100, 2] # insert
print(lst)

lst[2] = [100, 100, 100] # change
print(lst)


```

