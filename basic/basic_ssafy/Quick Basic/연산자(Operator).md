# 연산자(Operator)

## 산술연산자(Arithmetic Operators)

* 기본적인 사칙연산 가능함

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| *      | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| **     | 거듭제곱       |

```python
in : 
    print(5/2) # 2.5
    print(5//2) # 2
    print(5%2) # 1
```

* `divmod()` : 몫과 나머지를 출력하는 내장함수

  ```python
  in : 
      print(divmod(5, 2)) # (2, 1)
      q, r = divmod(5, 2)
      print(q, r) # 2 1
  ```

* 양수/음수 표현 가능

  ```python
  in : 
      num = 4
      print(-num)
  out : 
      -4
  ```

## 비교 연산자(Comparison Operators)

* 값을 비교할때 사용함
* 수학과 동일함

| 연산자 | 내용      |
| ------ | --------- |
| a > b  | 초과      |
| a < b  | 미만      |
| a >= b | 이상      |
| a <= b | 이하      |
| a == b | 같음      |
| a != b | 같지 않음 |

```python
in : 
    "hi" == "Hi"
out : 
    False
```

## 논리 연산자(Logical Operators)

| 연산자      | 내용                                 |
| ----------- | ------------------------------------ |
| `a` and `b` | `a`와 `b` 모두 True일 경우 True      |
| `a` or `b`  | `a`와 `b` 모두  False일 경우만 False |
| not `a`     | True => False, False => True         |

```python
in : 
    print(True and True) # True
    print(True and False) # False
    print(True or False) # True
    print(False or False) # False
    print(not True) # False
    print(not False) # True
```

* 모든 데이터를 **True**와 **False**로 나눌 수 있음

  * 정수형에서 0을 제외한 모든 수는 **True**

  ```python
  in : 
      print(3 and 0) # 0
      print(0 and 3) # 0
      print(3 or 4) # 3 #3과 4가 모두 True이지만 3이 앞에 있기에 출력됨
      print(-1 or 2) # -1 # 음수도 True
      print(-1 or 2) # 2
  ```

## 비트 연산자(Bitwise Operators)

| 연산자 | 내용                                                         |
| ------ | ------------------------------------------------------------ |
| &      | AND 연산. 둘 다 True이면 True                                |
| \|     | OR 연산. 둘 다 False이면 False                               |
| ^      | XOR 연산. 둘 중 하나만 True일 때 True                        |
| ~      | 보수 연산                                                    |
| <<     | 왼쪽 시프트 연산자. 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동 |
| `>>`   | 오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동 |

```python
a = 60, b = 13
a = 0011 1100
b = 0000 1101
(a & b) => 0000 1100 (12)
(a | b) => 0011 1101 (61)
(a ^ b) => 0011 0001 (49)
(~a)    => 1100 0011 (-61)
a << 2  => 1111 0000 (240)
a >> 2  => 0000 1111 (15)
```

## 복합 연산자(할당 연산자, Assignment Operators)

* 연산과 대입이 함께 이루어짐
* 반복문을 통해 갯수를 카운트하거나 할 때 가장 많이 활용됨

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **=b  | a = a ** b |

## 기타 연산자

### Concatenation

* 숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있음

  ```python
  in : 
      [1, 2, 4] + [3, 5, 7]
  out : 
      [1, 2, 4, 3, 5, 7]
  ```

### Containment Test

* `in` 연산자를 통해 속해있는지 여부를 확인할 수 있음

  ```python
  in : 
      "a" in "apple"
  out : 
      True
  ```

### Identity

* `is`연산자를 통해 동일한 object인지 확인할 수 있음

* `a is b` : `a`와 `b`의 주소(id)가 같은지 확인

  ```python
  in : 
      a = 3
  	b = 3
  	a is b
  	print(id(a), id(b)) # 1768147104 1768147104
  out : 
      True
  ```

### Indexing/Slicing

* `[]`를 통한 값 접근 및 `[:]`를 통한 슬라이싱



### 연산자 우선순위

1. `()`을 통한 grouping
2. Slicing
3. Indexing
4. 제곱연산자 **
5. 단항연산자 +, - (음수/양수 부호)
6. 산술연산자 *, /, %
7. 산술연산자 +, -
8. 비교연산자, `in`, `is`
9. `not`
10. `and`
11. `or`

