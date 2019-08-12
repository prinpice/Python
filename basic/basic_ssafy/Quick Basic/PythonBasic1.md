# Python

* 다른 언어들에 비해 직관적임



## 식별자

파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름이다.

- 식별자의 이름은 영문알파벳, _, 숫자로 구성된다.
- 첫 글자에 숫자가 올 수 없다.
- 대소문자를 구별한다.
- 아래의 예약어는 사용할 수 없다.

```
False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

jupyter에서 console안에서 입력후 실행할 때 : **shift + enter**

상단의 insert에서 insert cell을 클릭하여 python을 입력 후 실행해 볼 수 있다.

```python
# 어떤 keyword가 있는지 출력해보기

in : 
    import keyword
    print(keyword.kwlist)

out : 
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```



- 내장함수나 모듈 등의 이름으로도 만들면 안된다.
  - 내장함수 : 내부에 built-in되어있는 함수

```python
# 숫자를 문자로 바꿔주는 내장함수 : str
in : 
    str(5) # 5는 숫자
out : 
    5 #  문자
```



내장함수를 식별자로 선언하면 내장함수 기능이 없어져서 사용하지 못한다.

```python
in : 
    # str() 형변환 함수로 정해진 식별자로 변수를 할당해버리면, 함수호출이 되지 않음.
	str = 5
	str(5)
    
out : 
    TypeError                                 Traceback (most recent call last)
<ipython-input-3-ab0cf10527b7> in <module>
      1 # str() 형변환 함수로 정해진 식별자로 변수를 할당해버리면, 함수호출이 되지 않음.
      2 str = 5
----> 3 str(5)

TypeError: 'int' object is not callable
```



## 기초 문법



### 인코딩 선언

인코딩은 선언하지 않더라도 `UTF-8`로 기본 설정이 되어 있다.

만약, 인코딩을 설정하려면 코드 상단에 아래와 같이 선언한다. 주석으로 보이지만, Python `parser`에 의해 읽혀진다.

```python
# -*- coding; <....>
```





### 주석(Comment)

- 주석은 `#`으로 표현한다.

- `docstring`은 `"""`으로 표현한다.

  : 여러 줄의 주석을 작성할 수 있으며, 보통 함수/클래스 선언 다음에 해당하는 설명을 위해 활용한다.

```python
in : 
    # 이 줄을 실행되지 않습니다.
	def mysum(a, b):
    	"""이것은 덧셈함수입니다.
    	이 줄도 실행되지 않습니다."""
        
    mysum.__doc__ # 주석을 보여주는 함수
    
out : 
    '이것은 덧셈함수입니다.\n    이 줄도 실행되지 않습니다.'
```



### 코드 라인

- 기본적으로 파이썬에서는 `;` 을 작성하지 않는다.
- 한 줄로 표기할 떄는 `;`를 작성하여 표기할 수 있다.

```python
in : 
    print("hello") # hello
	print("world") # world
```

```python
in : 
    print("hello") print("world")
"""
      File "<ipython-input-9-391075056745>", line 1
    print("hello") print("world")
                       ^
SyntaxError: invalid syntax
"""
```

```python
in : 
    print("hello"); print("world") # hello
    							   # world
```



- 줄을 여러줄 작성할 때는 역슬래시`\`를 사용하여 아래와 같이 할 수 있다.
  - 줄이 길어질 때 가독성을 높이기 위해 사용한다.

```python
in : 
    a = 0
	if a\
	== 0 : 
    	print(a) # 0
```



- `[]` `{}` `()`는 `\` 없이도 가능하다.
  - [] : list자료형
  - {} : dictionary자료형
  - () : tuple자료형

```python
in : 
    lunch = ["짜장면", "탕수육", 
         	"깐풍기"]
```



### 변수(variable) 및 자료형

박스(dust)

dust는 60이다(x) / dust에 60을 저장한다(o)

- 변수는 `=`을 통해 할당(assignment) 된다. ( = : 할당문연산자)

- 해당 자료형을 확인하기 위해서는 `type()`을 활용한다.

- 해당 변수의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

  ( 변수에 값이 저장이 되는것이 아니라 값에 해당하는 주소를 저장한다.)

```python
in : 
    x = 1004
    print(x) # 1004
    print(id(x)) # 91060160
    type(x)
out : 
    int
```



- 같은 값을 동시에 할당할 수 있다.

```python
in : 
    w = t = 1004
    print(w, t) # 1004 1004
```



- 다른 값을 동시에 할당 가능하다.

```python
in : 
	x, y = 1, 2
	print(x, y) # 1 2
```



- 이를 활용하면 서로 값을 바꾸고 싶은 경우 아래와 같이 활용 가능하다.

```python
in : 
    # 쉽게 변수 값을 swap 가능함.
	print(x, y) # 1 2
	x, y = y, x
	print(x, y) # 2 1
```





## 수치형(Numbers)

### `int` (정수)

모든 정수는 `int`로 표현된다.

파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int` 형으로 표기 된다.

10진수가 아닌 8진수 : `0o`/2진수 : `0b` /16진수: `0x`로도 표현 가능하다.

```python
in : 
    a = 3
	type(a)
	b = 2**64 # 거듭제곱
	type(b)
    print(b) # 18446744073709551616
out : 
    int
    int
```

```python
# 보통 프로그래밍 언어 및 파이썬 2.x에서의 long은 OS 기준 32/64비트이다.
# 파이썬 3.x에서는 모두 int로 통합되었다.
```





**오버플로우** : 지정된 bit를 초과하는 경우

```python
# 파이썬은 기존 C 계열 프로그래밍 언어와 다르게 정수 자료형에서 오버플로우가 없다.
# arbitrary-precision arithmetic를 사용하기 때문이다. 

# int로 사용할 수 있는 최대공간
in : 
    import sys
	max_int = sys.maxsize
	print(max_int) # 2147483647
```



```python
in : 
    # n진수

	# 2진수
	binary_number = 0b10

	# 8진수
	octal_number = 0o10

	# 10진수
	decimal_number = 10

	# 16진수
	hexadecimal_number = 0x10
	print(binary_number, octal_number, decimal_number, hexadecimal_number)
    # 2 8 10 16
    print(f''' 2진수 : {binary_number}, 8진수 : {octal_number}''')
    # 2진수 : 2, 8진수 : 8
```



### `float`(부동소수점, 실수)

실수는 `float`로 표현된다.

다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않는다. (floating point rounding error)

이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있다.

**코딩을 할 때 최대한 float를 사용하지 않고 하는것이 중요!!!**

(소수점을 control하기 어렵기 때문)

```python
in : 
	a = 3.5
	type(a)
out : 
    float

```



- 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있다.

```python
in : 
    3.5 + 3.2
out : 
    6.7
```

소숫점을 bit공간에 할당할 때 정확한 값이 아니라 비슷한 값을 넣기 때문에 아래와 같이 출력된다.

```python
in : 
    3.5 - 3.12
out : 
    0.3799999999999999
```



소숫점을 사용하고 싶을 때 반올림(내장함수)을 사용한다.

```python
in : 
    round(3.5-3.12, 2)
out :
    0.38
```



```python
in : 
    0.1 * 3
out : 
    0.30000000000000004
```



```python
in : 
    a = 0.1 * 3
	b = 0.3

	a == b
out : 
    False
```



- 따라서 다음과 같은 방법으로 처리 할 수 있다. 이외에 다양한 방법이 있음

```python
in : 
    # 처리방법 1-1. 절대값을 비교
	a = 0.1 * 3
	b = 0.3

	abs(a-b) <= 1e-10
out :
    True
```

```python
# 처리방법 1-2. 절대값 비교를 내장된 float epsilon값과 비교
in : 
    import sys
	abs(a-b) <= sys.float_info.epsilon
out : 
    True
```

```python
# 처리방법 2. math 모듈을 통해 근사한 값인지 비교
# python 3.5부터는 math 모듈을 활용할 수 있다.
in : 
    import math
    math.isclose(a, b)
out : 
    True # 두 수가 같을정도로 가깝다
```



### `complex` (복소수)

복소수는 허수부를 `j`로 표현한다.

```python
in : 
    a = 3 -4j
    type(a)
out : 
    complex
```

```python
in : 
    print(a.real) # 3.0
    print(a.imag) # -4.0
    print(a.conjugate()) # (3+4j) # 켤레복소수
```





## Bool

파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있다.

비교/논리 연산을 수행 등에서 활용된다.

다음은 `False`로 변환됩니다.

```python
0, 0.0, (), [], {}, '', None
```

```python
in : 
    print(type(True)) # <class 'bool'>
```



- 형변환(Type Conversion)에서 추가적으로 다루는 내용입니다.





## None

파이썬에서는 값이 없음을 표현하기 위해 `None`타입이 존재합니다.

```python
in : 
    type(None)
out : 
    NoneType
```

```python
in : 
    a = None
    print(a) # None
```

빈공간을 채워서 관리할 때 많이 사용한다.



## 문자형(String)

### 기본 활용법

문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.

단, 문자열을 묶을 때 동일한 문장부호를 활용해야하며, `PEP-8`에서는 **하나의 문장부호를 선택**하여 유지하도록 하고 있습니다. (Pick a rule and Stick to it)

(**따옴표 개수 주의**)

```python
in : 
    greeting = 'hi'
    name = 'cm'
    print(greeting, name) # hi cm
    greeting + name
out : 
    'hicm'
```



- 다만 문자열 안에 문장부호(`'`, `"`)가 활용될 경우 이스케이프 문자(`\`)를 사용하는 것 대신 활용 가능 합니다.

```python
in : 
    print('철수가 말했다. '안녕?'') 
    """
      File "<ipython-input-50-4258189cde38>", line 1
    	print('철수가 말했다. '안녕?'')
                      ^
	SyntaxError: invalid syntax
    """
```

```python
in : 
    print('철수가 말했다. \'안녕?\'') # 철수가 말했다. '안녕?'
```



("")와 ('')가 서로 다르기 때문에 아래와 같이 사용할 수 있다.

```python
in : 
    print('철수가 말했다. "안녕?"') # 철수가 말했다. "안녕?"
    print("철수가 말했다. '안녕?'") # 철수가 말했다. '안녕?'
```



- 여러줄에 걸쳐있는 문장은 다음과 같이 표현 가능합니다.

`PEP-8`에 따르면 이 경우에는 반드시 `"""`를 사용하도록 되어 있습니다.

```python
in : 
    print("""
	개행문자 없이
	여러줄을 그대로 출력가능합니다.
	""")
    # 개행문자 없이
	# 여러줄을 그대로 출력가능합니다.
```



변수의 값이 계속 바뀌는 경우 string interpolation을 사용한다. => 아래 설명있음

```python
in :
    a = True
	print(f"""
	물론.
	string interpolation도 가능합니다.
	{a}!
	""")
    """
    물론.
	string interpolation도 가능합니다.
	True!
    """
```





### 이스케이프 문자열

문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분한다.

| 예약문자 | 내용(의미)      |
| -------- | --------------- |
| \n       | 줄바꿈          |
| \t       | 탭              |
| \r       | 캐리지리턴      |
| \0       | 널(Null)        |
| `\\`     | `\`             |
| '        | 단일인용부호(') |
| "        | 이중인용부호(") |

```python
in : 
    print("""
    개행문자 없이\n줄을 바꿀 수 있습니다.
    """)
    '''
    print("""
	개행문자 없이\n줄을 바꿀 수 있습니다.
	""")
    '''
```



- 이를 출력할 때 활용할 수가 있다.

```python
in : 
    print("개행문자 없이", end="\t"
	print("여러줄을 그대로 출력가능합니다")
    # 개행문자 없이	여러줄을 그대로 출력가능합니다.
```





### String interpolation

1) `%-formatting`

2) [`str.format()`](https://pyformat.info/)

3) [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 버전 이후에 지원 되는 사항입니다.

본 슬라이드에서는 `f-strings`의 기본적인 활용법만 알려드리고 나머지 `.format()`는 해당 [링크](https://pyformat.info/)에서 확인바랍니다.

```python
in : 
    name = "lee"
    "hello, %s" %name # %s, %f, %d 등을 '문자열포멧코'드라고 함
    f'hello, {name}'
out : 
    'hello, lee'
    'hello, lee'
```

```python
in : 
    name + name
    name * 3
out : 
    leelee
    leeleelee
```

- f-strings에서는 형식을 지정할 수 있으며,

```python
in : 
    "i eat %d apples" %5
out : 
    'i eat 5 apples'
```





- 연산도 가능합니다.

```python
in : 
    print("=" * 50)    # ==================================================
	print("myprogram") # myprogram
	print("=" * 50)	   # ==================================================
```



- 슬라이싱

```python
in : 
    a = "life is too short, you need Python"
	a[3]
    a[-1]
    a[0] + a[8]
    a[0:4] # 마지막은 출력이 되지 않는다.
    a[:6] # 처음부터 인덱스5까지 출력
    a[19:-6]
out : 
    e
    n
    'lt'
    'life'
    'you need '
```



datetime 클래스

```python
in : 
    import datetime
	today = datetime.datetime.now()
	print(today) # 2019-01-02 13:31:00.811371
    f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
out : 
    '오늘은 19년 01월 02일 Wednesday'
```



퍼센트(%) 출력

```python
in : 
    " error is %d%%." %98
out : 
    ' error is 98%.'
```



공백지정

```python
in : 
    "%10s" %'hi'
    "%-10s jane" %'hi'
out : 
    '        hi'
    'hi         jane'
```



소수점 지정

```python
in : 
    "%0.2f" %3.141592
out : 
    '3.14'
```

특정 글자 개수 반환

```python
in : 
    a = "hobby"
    a.count("b")
out : 
    2
```

특정 글자의 인덱스 반환

```python
in : 
    a.find("y")
out : 
    4
```

모든 문자를 대문자/소문자로 바꾸기

```python
in : 
    a = "hobby"
    a.upper()
    b = "HOBBY"
    b.lower()
out : 
    'HOBBY'
    'hobby'
```



- 양수/음수도 표현 가능합니다.



# 연산자

## 산술 연산자

Python에서는 기본적인 사칙연산이 가능합니다.

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



몫과 나머지를 출력하는 내장함수 : **divmod()**

```python
in : 
    print(divmod(5, 2)) # (2, 1)
    q, r = divmod(5, 2)
    print(q, r) # 2 1
```



- 양수/음수도 표현 가능합니다.

```python
in : 
    num = 4
    print(-num)
out : 
    -4
```





## 비교 연산자

우리가 수학에서 배운 연산자와 동일하게 값을 비교할 수 있습니다.

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |

```python
in : 
    "hi" == "Hi"
out : 
    False
```





## 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

우리가 보통 알고 있는 `&` `|`은 파이썬에서 비트 연산자이다.

```python
in : 
    print(True and True) # True
    print(True and False) # False
    print(True or False) # True
    print(False or False) # False
    print(not True) # False
    print(not False) # True
```





- 파이썬에서 and는 a가 거짓이면 a를 리턴하고, 참이면 b를 리턴한다.
- 파이썬에서 or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴한다.



**모든 데이터 타입을 참과 거짓으로 나눌 수 있다.**

정수형에서 0을 제외한 모든수는 참이다

```python
in : 
    print(3 and 0) # 0
    print(0 and 3) # 0
    print(3 or 4) # 3
    print(-1 or 2) # -1
    print(-1 or 2) # 2
```



## 복합 연산자

복합 연산자는 연산과 대입이 함께 이뤄진다.

가장 많이 활용되는 경우는 반복문을 통해서 갯수를 카운트하거나 할 때 활용된다.

| 연산자  | 내용       |
| ------- | ---------- |
| a += b  | a = a + b  |
| a -= b  | a = a - b  |
| a *= b  | a = a * b  |
| a /= b  | a = a / b  |
| a //= b | a = a // b |
| a %= b  | a = a % b  |
| a **= b | a = a ** b |









## 기타 연산자

### Concatenation

숫자가 아닌 자료형은 `+` 연산자를 통해 합칠 수 있다.

```python
in : 
    [1, 2, 4] + [3, 5, 7]
out : 
    [1, 2, 4, 3, 5, 7]
```



### Containment Test

`in` 연산자를 통해 속해있는지 여부를 확인할 수 있다.

```python
in : 
    "a" in "apple"
out : 
    True
```



### Identity

`is` 연산자를 통해 동일한 object인지 확인할 수 있다.

**a is b** : a와 b의 주소(id)가 같은지 다른지 확인

(나중에 Class를 배우고 다시 학습)

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

`[]`를 통한 값 접근 및 `[:]`을 통한 슬라이싱

(다음 챕터를 배우면서 추가 학습)







## 연산자 우선순위

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





# 기초 형변환(Type conversion, Typecasting)

파이썬에서 데이터타입은 서로 변환할 수 있다.

## 암시적 형변환(Implicit Type Conversion)

사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환 하는 경우이다. 아래의 상황에서만 가능하다.

- bool
- Numbers (int, float, complex)

```python
in : 
    True + 3
    type(True + 3)
    type(3.5 + 3)
out : 
    4
    int
    float
```





## 명시적 형변환(Explicit Type Conversion)

위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야한다.

- string -> integer : 형식에 맞는 숫자만 가능
- integer -> string : 모두 가능

암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능하다.

- `int()` : string, float를 int로 변환
- `float()` : string, int를 float로 변환
- `str()` : int, float, list, tuple, dictionary를 문자열로 변환

`list(), tuple()` 등은 다음 챕터에서 배울 예정이다.





# 시퀀스(sequence) 자료형

`시퀀스`는 데이터의 순서대로 나열된 형식을 나타낸다.

**주의! 순서대로 나열된 것이 정렬되었다라는 뜻은 아니다.**

파이썬에서 기본적인 시퀀스 타입은 다음과 같다.

1. 리스트(list)
2. 튜플(tuple)
3. 레인지(range)
4. 문자열(string)
5. 바이너리(binary) : 따로 다루지는 않습니다.



### list

**활용법**

```python
[value1, value2, value3]
```

리스트는 대괄호`[]` 를 통해 만들 수 있습니다.

값에 대한 접근은 `list[i]`를 통해 합니다.

```python
in : 
    l = []
    print(l) # []
    type(l)
out :
    list
```

```python
in : 
    lst = ["aaa", "bbb", "ccc"]
    lst[1] = "ddd"
    print(lst) # ['aaa', 'ddd', 'ccc']
```





### tuple

**활용법**

```python
(value1, value2)
```

튜플은 리스트와 유사하지만, `()`로 묶어서 표현합니다.

그리고 tuple은 수정 불가능(immutable)하고, 읽을 수 밖에 없습니다.

직접 사용하는 것보다는 파이썬 내부에서 사용하고 있습니다.

```python
in : 
    tuple_ex = (1, 2)
    print(type(tuple_ex)) # <class 'tuple'>
    
    is_tuple = 1, 2
    print(type(is_tuple)) # <class 'tuple'>
```



아래와 같은경우도 tuple에 해당되지만 잘 사용하지 않는다.

```python
in : 
    x, y = 1, 2
    x, y = y, x
```





### range()

레인지는 숫자의 시퀀스를 나타내기 위해 사용됩니다.

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다







## 시퀀스에서 활용할 수 있는 연산자/함수

| operation  | 설명                    |
| ---------- | ----------------------- |
| x in s     | containment test        |
| x not in s | containment test        |
| s1 + s2    | concatenation           |
| s * n      | n번만큼 반복하여 더하기 |
| s[i]       | indexing                |
| s[i:j]     | slicing                 |
| s[i:j:k]   | k간격으로 slicing       |
| len(s)     | 길이                    |
| min(s)     | 최솟값                  |
| max(s)     | 최댓값                  |
| s.count(x) | x의 갯수                |





# set, dictionary

- `set`과 `dictionary`는 기본적으로 순서가 없습니다.



### set

세트는 수학에서의 집합과 동일하게 처리됩니다.

세트는 중괄호`{}`를 통해 만들며, 순서가 없고 중복된 값이 없습니다.

**활용법**

```python
{value1, value2, value3}
```

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
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



- `set`을 활용하면 `list`의 중복된 값을 손쉽게 제거할 수 있습니다.





### dictionary

**활용법**

```python
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
```

- 딕셔너리는 `key`와 `value`가 쌍으로 이뤄져있으며, 궁극의 자료구조입니다.
- `{}`를 통해 만들며, `dict()`로 만들 수도 있습니다.
- `key`는 immutable한 모든 것이 가능하다. (불변값 : string, integer, float, boolean, tuple, range)
- `value`는 `list`, `dictionary`를 포함한 모든 것이 가능하다.

```python
in : 
    dic_a = {}
	print(type(dic_a)) # <class 'dict'>
```

```python
in : 
    phone_book = {'서울' : '02', '경기':'031'}
	phone_book.keys()
out : 
    dict_keys(['서울', '경기'])
```



# 정리

## 데이터 타입

**container** 

- **sequence(Ordered)**
  - 'String' (immutable)
  - [list] (mutable)
  - (tuple) (immutable)
  - range() (immutable)
- **Unordered**
  - {set} (mutable)
  - {dictionary:} (mutable)





**Quiz**

**두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.**

```python
n = 5
m = 9
print(('*'*n + '\n')*m)
```



**다음 딕셔너리에서 평균 점수를 출력하시오.**

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum = 0
for i in student.values():
    sum += i
print(sum/len(student))
```



**다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.**

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
## myway
a, b, o, ab = 0, 0, 0, 0
for i in blood_types:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'O':
        o += 1
    elif i == 'AB':
        ab += 1
print(f'A형 : {a}명, B형 : {b}명, AB형 : {ab}명, O형 : {o}명')

## p's way
result = {}
for bt in blood_types:
    if bt in result:
        result[bt] += 1
    else: 
        result[bt] = 1
print(result)
```





