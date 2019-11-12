# 자료형(data type)

## 수치형(Numbers)

### `int`(정수형)

* 모든 정수는 `int`로 표현

  * python 3.x 버전에서는 `long` 타입은 없고 모두 `int`형으로 표기됨

    ```python
    # 보통 프로그래밍 언어 및 파이썬 2.x에서의 long은 OS 기준 32/64비트이다.
    # 파이썬 3.x에서는 모두 int로 통합되었다.
    ```

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

* n진수 표현

  * 8진수 : `0o`
  * 2진수 : `0b`
  * 16진수 : `0x`

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

* overflow

  * 지정된 bit를 초과하는 경우

  * python은 arbitrary-precision arithmetic를 사용하기 때문에 overflow가 없음

    (기존 c 계열 프로그래밍 언어와 다름)

  ```python
  # int로 사용할 수 있는 최대공간
  in : 
      import sys
  	max_int = sys.maxsize
  	print(max_int) # 2147483647
  ```

### `float`(부동소수점, 실수형)

* 실수는 `float`로 표현

* floating point rounding error

  * 컴퓨터가 표현하는 과정에서 부동소수점을 사용하여(**소수점 control 어려움**) 항상 같은값으로 일치되지 않음

  * 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 발생하는 오류

  * 값이 같은지 비교하는 과정에서 문제 발생

    ```python
    in : 
        a = 0.1 * 3
    	b = 0.3
    
    	a == b
    out : 
        False
    ```

  **코딩을 할 때 최대한 float를 사용하지 않는것이 중요함!!!**

  ```python
  in : 
  	a = 3.5
  	type(a)
  out : 
      float
  ```

* 실제로 값을 처리하기 위해서 조심할 필요가 있음

  ```python
  in : 
      3.5 + 3.2
  out : 
      6.7
  ```

  소수점을 bit공간에 할당할 때 정확한 값이 아닌 비슷한 값을 넣기 때문에 아래와 같이 출력될 수 있음

  ```python
  in : 
      3.5 - 3.12
  out : 
      0.3799999999999999
  ```

* 소수점을 사용하고 싶을 때, `round()`(반올림, 내장함수) 를 사용

  ```python
  in : 
      round(3.5-3.12, 2)
  out :
      0.38
  ```

  사용하지 않을 경우

  ```python
  in : 
      0.1 * 3
  out : 
      0.30000000000000004
  ```

* 비교하는 방법(예시)

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

### `complex`(복소수)

* 허수부를 `j`로 표현

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

### `Bool`

* `True`와 `False`로 이루어져있음

  ```python
  in : 
      print(type(True)) # <class 'bool'>
  ```

* 비교/논리 연산 수행 등에서 활용

* `False`로 변환되는 경우

  ```python
  0, 0.0, (), [], {}, '', None
  ```

* 형변환(Type Conversion)에서 추가적으로 다루는 내용

### None

* python에서는 `None`타입이 존재함

  ```python
  in : 
      type(None)
  out : 
      NoneType
  ```

* 값이 없음을 표현

* 빈공간을 채워서 관리할 때 많이 사용함

  ```python
  in : 
      a = None
      print(a) # None
  ```



## 문자형(String)

* Single quites(`''`) 또는 Double quotes(`""`)를 활용하여 표현(단, 하나의 문장부호를 선택, Pick a rule and Stick to it)

* 따옴표 개수 주의

  ```python
  in : 
      greeting = 'hi'
      name = 'cm'
      print(greeting, name) # hi cm
      greeting + name
  out : 
      'hicm'
  ```

* 문자열 안에 문장부호(`''`, `""`)가 활용될 경우 이스케이프 문자(`\`)를 사용하는 것 대신 활용 가능함

  * 동일 문장부호 사용할 경우

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

  * 이스케이프 문자(`\`)사용할 경우

  ```python
  in : 
      print('철수가 말했다. \'안녕?\'') # 철수가 말했다. '안녕?'
  ```

  * 다른 문장부호 사용할 경우

  ```python
  in : 
      print('철수가 말했다. "안녕?"') # 철수가 말했다. "안녕?"
      print("철수가 말했다. '안녕?'") # 철수가 말했다. '안녕?'
  ```

* 여러줄에 걸쳐있는 문장은 `""" """`를 사용하여 표현 가능함(개행문자 필요X)

  ```python
  in : 
      print("""
  	개행문자 없이
  	여러줄을 그대로 출력가능합니다.
  	""")
      # 개행문자 없이
  	# 여러줄을 그대로 출력가능합니다.
  ```

* 변수의 값이 계속 바뀌는 경우 `string interpolation`을 사용

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

* 연산

  ```python
  in : 
      print("=" * 50)    # ==================================================
  	print("myprogram") # myprogram
  	print("=" * 50)	   # ==================================================
  ```

  ```python
  in : 
      name + name
      name * 3
  out : 
      leelee
      leeleelee
  ```

* 슬라이싱

  ```python
  in : 
      a = "life is too short, you need Python"
  	a[3]
      a[-1]
      a[0] + a[8]
      a[0:4] # 마지막은 출력이 되지 않는다.index가 0, 1, 2, 3에 해당하는 값만 출력됨
      a[:6] # 처음부터 인덱스5까지 출력
      a[19:-6]
  out : 
      e
      n
      'lt'
      'life'
      'you need '
  ```

### 문자열에 사용되는 함수(function)

* `count()` : 특정 글자 개수를 반환함

  ```python
  in : 
      a = "hobby"
      a.count("b")
  out : 
      2
  ```

* `find()` : 특정 글자의 인덱스를 반환함

  ```python
  in : 
      a.find("y")
  out : 
      4
  ```

* `upper()` : 모든 문자를 대문자로 바꿈

  ```python
  in : 
      a = "hobby"
      a.upper()
  out :
      'HOBBY'
  ```

* `lower()` : 모든 문자를 소문자로 바꿈

  ```python
  in :
      b = "HOBBY"
      b.lower()
  out :
      'hobby'
  ```

### 이스케이프 문자열

* 문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위해 사용됨
* `\`을 활용하여 구분함

| 예약문자 | 내용(의미)        |
| -------- | ----------------- |
| \n       | 줄바꿈            |
| \t       | 탭                |
| \r       | carriage return   |
| \0       | Null              |
| `\\`     | `\`               |
| `\'`     | 단일인용부호(`'`) |
| `\"`     | 이중인용부호(`"`) |

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

```python
in : 
    print("개행문자 없이", end="\t")
	print("여러줄을 그대로 출력가능합니다")
    # 개행문자 없이	여러줄을 그대로 출력가능합니다.
```

### String Interpolation

* `%-formatting`

  * 문자열 포멧코드 : `%s`, `%f`, `%d` 등등

  ```python
  in : 
      name = "lee"
      "hello, %s" %name
  out :
      'hello, lee'
  ```

  * 퍼센트(%) 출력

    ```python
    in : 
        " error is %d%%." %98
    out : 
        ' error is 98%.'
    ```

  * 공백지정

    ```python
    in : 
        "%10s" %'hi'
        "%-10s jane" %'hi'
    out : 
        '        hi'
        'hi         jane'
    ```

  * 소수점 지정

    ```python
    in : 
        "%0.2f" %3.141592
    out : 
        '3.14'
    ```

* `str.format()`

  ```python
  in :
      name = "lee"
      "hello, {}".format(name)
  out :
      'hello, lee'
  ```

* `f-strings` : python 3.6버전 이상 지원

  ```python
  in :
      name = "lee"
      f'hello, {name}'
  out :
      'hello, lee'
  ```

  * `datatime`클래스를 사용할 경우

    ```python
    in : 
        import datetime
    	today = datetime.datetime.now()
    	print(today) # 2019-01-02 13:31:00.811371
        f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}'
    out : 
        '오늘은 19년 01월 02일 Wednesday'
    ```

    