# 함수(function)

## 들어가기 전

**직사각형의 둘레와 면적을 구하는 코드를 작성해주세요.**

```python
height = 30
width = 20
```

```
예시 출력)
직사각형 둘레: 100, 면적, 600입니다.
```

```python
in : 
    height = 30
    width = 20
    # 아래에 코드를 작성하세요.
    round_re = 2 * (height + width)
    s = height * width
    print(f'직사각형 둘레: {round_re}, 면적: {s}입니다.')
out : 
    직사각형 둘레: 100, 면적: 600입니다.
```

* 앞서 작성한 코드에서 매번 사각형의 둘레와 면적을 구하기 위해서는 변수에 값을 바꾸거나 코드를 복사/붙여넣기 해야함

* 코드가 많아질수록 문제가 발생할 확률이 높아지며, 유지 보수하기도 힘들어짐

  **E = MC^2^**(Error = more code2)

  **Programming Principle**

  **K**EEP     **D**on't        **K**EEP

  **I**T           **R**epeat     **I**T

  **S**IMPLE  **Y**ourself  **S**HORT

  **S**TUPID                   **S**IMPLE



## 개요

```python
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

* 선언
  * `def`로 시작하여 `:`으로 끝남
  * `4spaces 들여쓰기`로 코드 블럭을 생성
* 매개변수(parameter)를 넘겨줄 수 있음
* 동작 후에 return을 통해 결과값 전달 가능(return 값 없으면, None을 반환함)
* 호출
  * `func(val1, val2)`
* 내장함수
  * `dir(__builtins__)`으로 확인 가능

### return

* 함수의 반환되는 값
* 객체종류 무관
* 하나의 객체만 반환
* return되면 함수를 호출한 곳으로 돌아감

### 인자/인수

* 함수는 인자(parameter)를 받을 수 있음

#### 위치 인수

* 함수는 기본적으로 인수를 위치로 판단함

  ```python
  def my_sum(a, b):
      return a + b
  
  def my_sum(a, b):
      a = 3
      b = 5
      return a + b
  
  my_sum(3, 5) => a + b => 8
  ```

### 기본값(Default Argument Values)

* 함수가 호출될 때, 인자를 지정하지 않아도 기본값 설정 가능

  ```python
  def func(p1=v1):
      return p1
  ```

  ```python
  in : 
      def my_sum(a, b = 5):
      return a + b
      my_sum(2, 4)
      my_sum(3)
  out : 
      6
      8
  ```

* 기본 인자 값이 설정되어 있어도, 기존의 함수와 동일하게 호출 가능함

  ```python
  def my_sum(a, b=0):
      return a + b
  
  def my_sum(a, b=0):
      a = 3
      b = 5
      return a + b
  
  my_sum(3, 5) => a + b => 8
  ```

* 호출시 인자가 없으면 기본 인자 값이 활용됨

  ```python
  def my_sum(a, b=0):
      return a + b
  
  def my_sum(a, b=0):
      a = 0
      b = 3
      return a + b
  
  my_sum(3) => a + 0 => 3
  ```

* 단, 기본 매개변수 이후에 기본 값이 없는 매개변수는 사용불가능

### 키워드 인자(Keyword Arguments)

* 키워드 인저는 직접적으로 변수의 이름으로 특정 인자 전달 가능

  ```python
  # 키워드 인자 예시
  def greeting(age, name='ssafy'):
      print(f'{name}은 {age}살입니다.')
  
  # 다양하게 함수를 호출해봅시다.
  ```

* 단, 키워드 인자를 활용한 뒤에 위치 인자 활용 불가능

  ```python
  in : 
      # 오류를 확인해봅시다.
  	def greeting(name="ssafy", age):
      	print(f'{name}은 {age}입니다.')
  out : 
  	File "<ipython-input-25-2441bfdfc7c5>", line 2
        def greeting(name="ssafy", age):
                   ^
    SyntaxError: non-default argument follows default argument
      
  # 정상적인 코드로 바꿔봅시다.
  def greeting(age, name='ssafy'):
      print(f'{name}은 {age}입니다.')
  ```

### 가변 인자 리스트

* 정해지지 않은 임의의 숫자의 인자를 받기 위해 사용함

* tuple형태로 처리되며, `*`로 표현함

  ```python
  def func(*args):
  ```

  ```python
  in : 
      def sum_mul(choice, *args):
          if choice == "sum":
              result = 0
              for i in args:
                  result = result + i
          elif choice == "mul":
              result = 1
              for i in args:
                  result = result * i
          return result
  
      sum_mul("mul", 1, 2, 3)
  out : 
      6
  ```

### 정의되지 않은 인자들 처리하기

* 정의되지 않은 인자들은 **dict**형태로 처리되며, `**`로 표현함

* 주로 **kwargs**라는 이름 사용

* **\**kwargs**를 통해 인자를 받아 처리 가능

  ```python
  def func(**kwargs):
  ```

#### dict()

* dictionary를 새로 생성할 때 사용함
* 파이썬 표준 라이브러리의 내장함수 중 하나
* 딕셔너리 클래스
* 구성
  * class **dict**(**kwarg)
  * class **dict**(mapping, **kwarg)
  * class **dict**(iterable, **kwarg)

#### dictionary를 인자로 넘기기(unpackin arguments list)

* `**dict`를 통해 함수에 인자를 넘길 수 있음

  ```python
  in : 
      # user 검증(유사 회원가입)을 작성해보세요.
  # username, password, password_confirmation을 받아서 비밀번호 일치 여부를 판단해보세요.
  
  def user(username, password, password_confirmation):
      if password == password_confirmation:
          print(f'{username}님, 회원가입이 완료되었습니다.')
      else:
          print('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
  my_account = {
      'username':'홍길동',
      'password':'1q2w3e4r',
      'password_confirmation':'1q2w3e4r'
  }
                
  user(**my_account)
  out : 
      홍길동님, 회원가입이 완료되었습니다.
  ```

### url 생성

* url 패턴을 만들어 문자열을 반환하는 `my_url` 함수를 만들어봅시다. 영진위에서 제공하는 일별 박스오피스 API 서비스는 다음과 같은 방식으로 요청을 받습니다.

  ```
  기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?
  ```

  * key : 발급받은 키 값(abc)
  * targetDt: yyyymmdd
  * itemPerPage: 1~10 **기본 10**

  ```
  예시)
  호출 1)
  my_url(key='abc', targetDt='yyyymmdd')
  
  호출 2)
  api = {
      'key': 'abc',
      'tagetDt': 'yyyymmdd'
  }
  my_url(**api)
  
  예시 출력)
  'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?itemPerPage=10key=abc&tagetDt=yyyymmdd&'
  ```

### url 검증

* 만들어진 요청을 보내기 전에 URL을 검증해야 함

  ```
  > 아래의 두가지 상황만 만들도록 하겠습니다. <
  
  key, targetDt가 없으면, '필수 요청변수가 누락되었습니다.'
  
  itemPerPage의 범위가 1~10을 넘어가면, '1~10까지의 값을 넣어주세요.'
  ```

### 이름공간 및 스코프(Scope)

* 파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있고, LEGB Rule을 가지고 있음

* 변수에서 값을 찾을 때 순서

  * **L**ocal scope : 정의된 함수
    * 수명주기 : 함수가 실행된 시점 이후부터 리턴할 때까지
  * **E**nclosed scope : 상위 함수
    * 수명주기 : 함수가 실행된 시점 이후부터 리턴할 때까지
  * **G**lobal scope : 함수 밖의 변수 혹은 import된 모듈
    * 수명주기 : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
  * **B**uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
    * 파이썬이 실행된 이후부터 끝까지

  ```python
  in : 
      # 프린트 하는 함수를 만들어서 자세히 확인해봅시다.
      a = 1 # Global 변수 a
      def localscope(a): # Local 변수 a
          print(a)
      localscope(3)
  out : 
      3    
  ```

  ```python
  in : 
      # 전역 변수를 바꿀 수 있을 까요?
      a = 1
      def localscope(a):
          a = 5
          print(a)
      localscope(5)
      print(a)
  out : 
      5
      1
  ```

  ```python
  in : 
      # 굳이 전역에 있는 변수를 바꾸고 싶다면, 아래와 같이 선언할 수 있습니다. 단, 사용하지마세요 
      a = 1
      def localscope(a):
          global a = 5
          print(a)
      localscope(5)
      print(a)
  out : 
      File "<ipython-input-51-7e72bb4b2a4d>", line 4
          global a = 5
                   ^
      SyntaxError: invalid syntax
  ```

  ```python
  # scope youtube embed
  # from IPython.display import YouTubeVideo
  YouTubeVideo('yH_1vwnp3ZQ', width='100%')
  ```

  

