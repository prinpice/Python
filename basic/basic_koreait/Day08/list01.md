# list01

```python
"""
# 리스트
1. 여러개의 대상을 묶어서 저장하는것을 의미한다
2. 리스트 만드는법:
    리스트변수 = [요소1 , 요소2 , 요소3]
3. 리스트의 특징:
    1) 리스트의 크기는 제한이 없다.
    2) 리스트 안에는 어떠한 자료형도 포함시킬수 있다.
    3) 객수에 따라 방번호(인덱스)가 매겨진다 (인덱스는 0부터 시작한다)
4. 리스트 사용방법 ==> [] 대괄호로 접근한다.
    변수 + [인덱스번호]
"""
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1) # [1, 2, 3, 4, 5, 6, 7]
print(list1[0]) # 1
# 문제 1) 7을 출력해보세요
print(list1[6]) # 7
# 전체 출력 ==> while
num = 0
while num < 7:
    if num < 6:
        print(list1[num], ", ", end="")
    else:
        print(list1[num])
    num += 1
```

