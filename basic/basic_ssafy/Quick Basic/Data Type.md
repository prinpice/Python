# Data Type

* container
  * **sequence(Ordered)**
    * 'String' (immutable)
    * [list] (mutable)
    * (tuple) (immutable)
    * range() (immutable)
  * **Unordered**
    - {set} (mutable)
    - {dictionary:} (mutable)

## 시퀀스 자료형(Sequence Data Type)

* `sequence` : 데이터의 순서대로 나열된 형식(**정렬X**)
* 순서가 있음(ordered)

### list

* 대괄호`[]`를 통해 생성

  ```python
  [value1, value2, value3, ...]
  ```

  ```python
  in : 
      l = []
      print(l) # []
      type(l)
  out :
      list
  ```

* mutable

* 값에 대한 접근은 `list[i]` 사용함

  ```python
  in : 
      lst = ["aaa", "bbb", "ccc"]
      lst[1] = "ddd"
      print(lst) # ['aaa', 'ddd', 'ccc']
  ```

### tuple

* 소괄호`()`로 묶어서 표현함

* 리스트와 유사

* 생성 후 수정 불가(immutable), 읽기만 가능

* 직접 사용하기 보다는 파있너 내부에서 사용하고 있음

  ```python
  in : 
      tuple_ex = (1, 2)
      print(type(tuple_ex)) # <class 'tuple'>
      
      is_tuple = 1, 2
      print(type(is_tuple)) # <class 'tuple'>
  ```

* 변수의 값을 교환하는 경우도 tuple에 해당됨(사용빈도 낮음)

  ```python
  in : 
      x, y = 1, 2
      x, y = y, x
  ```

### range()

* 숫자의 시퀀스를 나타내기 위해 사용됨
* immutable
* 기본형 : `range(n)`
  * `0`부터 `n-1`까지 값을 가짐
* 범위 지정 : `range(n, m)`
  * `n`부터 `m-1`까지 값을 가짐
* 범위 및 스텝 지정 : `range(n, m, s)`
  * `n`부터 `m-1`까지 `+s`만큼 증가함

### 시퀀스에서 활용 가능한 연산자/함수

| operation  | 설명                    |
| ---------- | ----------------------- |
| x in s     | containment test        |
| x not in s | containment test        |
| s1 + s2    | concatenation           |
| s * n      | n번만큼 반복하여 더하기 |
| s[i]       | indexing                |
| s[i:j]     | slicing                 |
| s[i:j:k]   | k 간격으로 slicing      |
| len(s)     | 길이                    |
| min(s)     | 최솟값                  |
| max(s)     | 최댓값                  |
| s.count(x) | x의 갯수                |

## 순서가 없는 자료형(Unordered)

### set

* 중괄호 `{}`를 통해 생성

  ```python
  {value1, value2, vlaue3, ...}
  ```

* mutable

* 순서가 없고 **중복된 값이 없음**

  * set을 활용하여 list의 중복된 값을 손쉽게 제거 가능함

  ```python
  in : 
      print(set([1, 2, 3, 3, 4]))
  out :
      {1, 2, 3, 4}
  ```

| 연산자/함수       | 내용   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합잡합 |
| a & b             | 교집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

```python
in : 
    set_a = {1, 2, 3}
    set_b = {3, 5, 6}
    print(set_a - set_b) # {1. 2}
    print(set_a | set_b) # {1, 2, 3, 5, 6}
	print(set_a & set_b) # {3}
	print(set_a.union(set_b)) # {1, 2, 3, 5, 6}
	print(set_a.intersection(set_b)) # {3}
```

### dictionary

* `key`, `value`쌍으로 이루어져 있음

* 궁극의 자료구조

* mutable

* 중괄호 `{}` 또는 `dict()`를 통해 생성

  ```python
  in : 
      dic_a = {}
  	print(type(dic_a)) # <class 'dict'>
  ```

* `key`는 **immutable**한 모든 것이 가능함

  (불변값 : string, integer, float, boolean, tuple, range)

* `value`는 `list`, `dictionary`를 포함한 모든것이 가능함

  ```python
  in : 
      phone_book = {'서울' : '02', '경기':'031'}
  	phone_book.keys()
  out : 
      dict_keys(['서울', '경기'])
  ```

  