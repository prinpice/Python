# python_3

# 함수(function) 기초



**INPUT x** -> **FUNCTION f:** -> **OUTPUT f(x)**



## 들어가기전에

> 직사각형의 둘레와 면적을 구하는 코드를 작성해주세요.

```python
height = 30
width = 20
```

------

```
예시 출력)
직사각형 둘레: 100, 면적: 600입니다.
```

```python
height = 30
width = 20
# 아래에 코드를 작성하세요.
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



- 앞서 작성한 코드에서 매번 사각형의 둘레와 면적을 구하기 위해서는 변수에 값을 바꾸거나 코드를 복사 붙여넣기 해야합니다.
- 코드가 많아질수록 문제가 발생할 확률이 높아지며, 유지 보수하기도 힘들어진다.



**E = MC^2**

Error = more code2

**Programming Principle**

**K**EEP       **D**on't	   **K**EEP

**I**T		 **R**epeat	   **I**T

**S**IMPLE    **Y**ourself   **S**HORT 

**S**TUPID			   **S**IMPLE





## 개요

**활용법**

```
def func(parameter1, parameter2):
    code line1
    code line2
    return value
```

- 함수 선언은 `def`로 시작하여 `:`으로 끝나고, 다음은 `4spaces 들여쓰기`로 코드 블록을 만듭니다.
- 함수는 `매개변수(parameter)`를 넘겨줄 수도 있습니다.
- 함수는 동작후에 `return`을 통해 결과값을 전달 할 수도 있습니다. (`return` 값이 없으면, None을 반환합니다.)
- 함수는 호출을 `func(val1, val2)`와 같이 합니다.



```python
# 위의 사각형 코드를 rectangle() 함수로 만들어보세요.
def rectangle(height, width):
    round_re = 2*(height + width)
    s = height * width
    print(f'직사각형 둘레: {round_re}, 면적: {s}입니다.')
    return
```

```python
in : 
    # 너비 30, 높이 100일때 호출 해보세요
    height = 30
    width = 100
    rectangle(30, 100)
out : 
    직사각형 둘레: 260, 면적: 3000입니다.
```



**INPUT x** -> **FUNCTION f:** -> **OUTPUT f(x)**

**INPUT x** : parameter(매개변수)

**OUTPUT f(x)** : return value



ex) 

**menu=["라면", "김밥", "떡볶이", "순대"]** => **random.choice(menu)** => **김밥**

**random.choice(menu)** 에서 **menu** : parameter(매개변수)

**김밥** : return value



**Built-in Functions**

| abs() |      |      |      |      |
| ----- | ---- | ---- | ---- | ---- |
| all() |      |      |      |      |
| any() |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |
|       |      |      |      |      |



```python
# 내장함수 목록을 직접 볼 수도 있습니다.
dir(__builtins__)
```



# 함수의 return

앞서 설명한 것과 마찬가지로 함수는 반환되는 값이 있으며, 이는 어떠한 종류의 객체여도 상관없습니다.

단, 오직 한 개의 객체만 반환됩니다.

함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아갑니다.



## 실습문제

> 아래의 코드와 동일한 `my_max`함수를 만들어주세요.
>
> 정수를 두개 받아서, 큰 값을 반환합니다.

```python
max(1, 5)
```

```
예상 출력)
5
```

```python
max(1,5)
```

```python
# 여기에 my_max 함수를 만들어주세요.
def my_max(a, b):
    if(a >= b):
        return a
    else:
        return b
```

```python
in : 
    # 만든 함수를 호출해보세요.
	print(my_max(1, 5))
out : 
    5
```



## 실습문제

> 함수는 모든 객체를 리턴할 수 있습니다.
>
> 리스트 두개를 받아 각각 더한 결과를 비교하여 값이 큰 리스트를 반환합니다.

```python
my_list_max([10, 3], [5, 9])
```

```
예상 출력)
[5, 9]
```

```python
# 여기에 my_max 함수를 만들어주세요.
def my_list_max(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for i in lst2:
        sum2 += i
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
    
# 여기에 my_max 함수를 만들어주세요.
def my_list_max(lst1, lst2):
    if sum(lst1) >= sum(lst2):
        return lst1
    else:
        return lst2
```

```python
in : 
    # 만든 함수를 호출해보세요.
	my_list_max([10, 3], [5, 9])
out :
    [5, 9]
```





# 함수의 인자/인수

함수는 `인자(parameter)`를 받을 수 있습니다.

## 위치 인수

함수는 기본적으로 인수를 위치로 판단합니다.



def my_sum(a, b):

​	return a + b



def my_sum(a, b):

​	*a = 3*

​	*b = 5*

​	return a + b



**my_sum(3, 5)** -> **a + b** -> **8**



## 기본 값(Default Argument Values)

함수가 호출될 때, 인자를 지정하지 않아도 기본 값을 설정할 수 있습니다.

**활용법**

```
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





* 기본 인자 값이 설정되어 있더라도 기존의 함수와 동일하게 호출 가능합니다.

def my_sum(a, b=0):

​	return a + b



def my_sum(a, b=0):

​	*a = 3*

​	*b = 5*

​	return a + b



**my_sum(3, 5)** -> **a + b** -> **8**



* 호출시 인자가 없으면 기본 인자 값이 활용됩니다.

def my_sum(a, b=0):

​	return a + b



def my_sum(a, b=0):

​	*a = 0*

​	*b = 3*

​	return a + b



**my_sum(3)** -> **a + 0** -> **3**





- 단, 기본 매개변수 이후에 기본 값이 없는 매개변수를 사용할 수는 없습니다.

## 키워드 인자(Keyword Arguments)

키워드 인자는 직접적으로 변수의 이름으로 특정 인자를 전달할 수 있습니다.

```python
# 키워드 인자 예시
def greeting(age, name='ssafy'):
    print(f'{name}은 {age}살입니다.')

# 다양하게 함수를 호출해봅시다.
```



- 단 아래와 같이 활용할 수는 없습니다. 키워드 인자를 활용한 뒤에 위치 인자를 활용할 수는 없습니다.

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

```

```python
# 정상적인 코드로 바꿔봅시다.
def greeting(age, name='ssafy'):
    print(f'{name}은 {age}입니다.')
```





우리가 주로 활용하는 `print()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다.



**print** (*objects, sep='', end='\n', file=sys.stdout, flush=False)

​	*objects*를 텍스트 스트림 *file*로 인쇄하는데, *sep*로 구분되고 *end*를 뒤에 붙입니다. 있다면 , *sep*, *end*, *file* 및 *flush*는 반드시 키워드 인자로 제공해야 합니다.



​	모든 비 키워드 인자는 **str()** 이 하듯이 문자열로 변환된 후 스트림에 쓰이는데,  *sep*로 구분되고 *end*를 뒤에 붙입니다. *sep*과 *end*는 모두 문자열이어야 합니다; **None**일 수도 있는데, 기본값을 사용한다는 뜻입니다. *objects*가 주어지지 않으면 **print()**는 *end*만 씁니다.



​	*file* 인자는 **write(string)** 메서드를 가진 객체여야 합니다; 존재하지 않거나 **None**이면, **sys.stdout**이 사용됩니다. 인쇄된인자는 텍스트 문자열로 변환되기 때문에, **print()** 는 바이너리 모드 파일 객체와 함께 사용할 수 없습니다. 이를 위해서는, 대신 **file.write(...)**를 사용합니다.



​	출력의 버퍼링 여부는 일반적으로 *file* 에 의해 결정되지만, *flush* 키워드 인자가 참이면 스트림이 강제로 플러시 됩니다.



​	*버전 3.3으로 변경: flush 키워드 인자가 추가되었습니다.*

```python
print('hi', end='_')
print('hello', end='_')
```

```python
hi_hello_
```





## 가변 인자 리스트

앞서 설명한 `print()`처럼 정해지지 않은 임의의 숫자의 인자를 받기 위해서는 가변인자를 활용합니다.

가변인자는 `tuple` 형태로 처리가 되며, `*`로 표현합니다.

**활용법**

```
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





### 실습문제

> 정수를 여러 개 받아서 가장 큰 값을 반환(return)하는 `my_max()`을 만들어주세요.

```python
my_max(10, 20, 30, 50)
```

------

```
예시출력)
50
```

```python
max(1, 2, 3, 4)
```

```python
# 아래에 코드를 작성해주세요.
def my_max(*args):
    return max(args)
```

```python
in : 
    # 만든 함수를 호출해보세요.
	my_max(1, 2, 3, 4)
out : 
    4
```

```python
in : 
    # 아래에 코드를 작성해주세요.
    def my_max(*args):
        result = 0
        for idx, val in enumerate(args):
            if idx == 0:
                result = val
            else:
                if val > result:
                    result = val
        return result
    my_max(1, 2, 9, 3, 4, 5)    
out : 
    9
```



## 정의되지 않은 인자들 처리하기

정의되지 않은 인자들은 `dict` 형태로 처리가 되며, `**`로 표현합니다.

주로 `kwagrs`라는 이름을 사용하며, `**kwargs`를 통해 인자를 받아 처리할 수 있습니다.

**활용법**

```
def func(**kwargs):
```



우리가 dictionary를 만들 때 사용할 수 있는 `dict()` 함수는 [파이썬 표준 라이브러리의 내장함수](https://docs.python.org/ko/3.6/library/functions.html)중 하나이며, 다음과 같이 구성되어 있다. 



*class* **dict** (**kwarg)

*class* **dict** (mapping, **kwarg)

*class* **dict** (iterable, **kwarg)

​	새 딕셔너리를 만듭니다. **dict** 객체는 딕셔너리 클래스입니다.

### 실습문제

> `my_dict()` 함수를 만들어 실제로 dictionary 모습으로 출력 함수를 만들어보세요.

```
예시 출력)
한국어: 안녕, 영어: hi
```



```python
# 아래에 코드를 작성해주세요.
def my_fake_dict(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f'{key}, {value}')
    print(', '.join(result))
```

```python
in : 
    # 만든 함수를 호출해보세요.
	my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
out : 
    한국어, 안녕, 영어, hi, 독일어, Guten Tag
```

```python
# 사실은 dict()는 출력이 아니라 딕셔너리를 리턴합니다. 
# 리턴하는 my_fake_dict를 만들어주세요.        
def my_fake_dict(**kwargs):
    result = []
    for key, value in kwargs.items():
        result.append(f'{key}, {value}')
    return result
```

```python
in : 
    # 만든 함수를 호출해보세요.
	my_fake_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag')
out : 
    ['한국어, 안녕', '영어, hi', '독일어, Guten Tag']
```





## dictionary를 인자로 넘기기(unpacking arguments list)

`**dict`를 통해 함수에 인자를 넘길 수 있습니다.

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




  



### 실습문제 URL 편하게 만들기

> url 패턴을 만들어 문자열을 반환하는 `my_url` 함수를 만들어봅시다.
>
> 영진위에서 제공하는 일별 박스오피스 API 서비스는 다음과 같은 방식으로 요청을 받습니다.

```
기본 요청 URL : http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?
```

- key : 발급받은 키값(abc)
- targetDt : yyyymmdd
- itemPerPage : 1 ~ 10 **기본 10**

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











### URL 검증하기

> 이제 우리는 만들어진 요청 보내기전에 URL을 검증해야합니다.
>
> 앞선 설명을 참고하여 검증 로직을 구현하고 문자열을 반환하세요.

```
> 아래의 두가지 상황만 만들도록 하겠습니다. <

key, targetDt가 없으면, '필수 요청변수가 누락되었습니다.'

itemPerPage의 범위가 1~10을 넘어가면, '1~10까지의 값을 넣어주세요.'
```







## 이름공간 및 스코프(Scope)

파이썬에서 사용되는 이름들은 이름공간(namespce)에 저장되어 있습니다. 그리고, LEGB Rule을 가지고 있습니다.

변수에서 값을 찾을 때 아래와 같은 순서대로 이름을 찾아나갑니다.

- `L`ocal scope: 정의된 함수
- `E`nclosed scope: 상위 함수
- `G`lobal scope: 함수 밖의 변수 혹은 import된 모듈
- `B`uilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성





- `str()` 코드가 실행되면
- str을 Global scope에서 먼저 찾아서 `str = 4`를 가져오고,
- 이는 함수가 아니라 변수이기 때문에 `not callable`하다라는 오류를 내뱉게 됩니다.
- 우리가 원하는 `str()`은 Built-in scope에 있기 때문입니다.

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



이름공간은 각자의 수명주기가 있습니다.

- built-in scope : 파이썬이 실행된 이후부터 끝까지
- Global scope : 모듈이 호출된 시점 이후 혹은 이름 선언된 이후부터 끝까지
- Local/Enclosed scope : 함수가 실행된 시점 이후부터 리턴할때 까지







## function_problem

[![Jupyter Notebook](http://localhost:8888/static/base/images/logo.png?v=641991992878ee24c6f3826e81054a0f)](http://localhost:8888/tree?token=9a4b7209c91577f232af352de0d028ac9e1000c892a0c4a6)

function-problems1(unsaved changes)

![Current Kernel Logo](http://localhost:8888/kernelspecs/python3/logo-64x64.png)

Logout



Python 3 



Not Trusted

- [File](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Edit](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [View](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Insert](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Cell](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Kernel](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Widgets](http://localhost:8888/notebooks/function-problems1.ipynb#)
- [Help](http://localhost:8888/notebooks/function-problems1.ipynb#)









Run







## 함수 문제 set 1



### 문제1

> 2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 두 수 a,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WEB,THU,FRI,SAT입니다.

> 예를 들어, a=5,b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.

```python
in : 
    #여기에 코드를 작성하세요
    def week(a, b):
        m = 1
        d = 1
        weekd = 'FRI'
        week_lst = ['SUN', 'MON', 'TUE','WEB','THU','FRI','SAT']
        tot = -1
        for i in range(m, a):
            if i == 2:
                tot += 29
            elif i in (4, 6, 9, 11):
                tot += 30
            else:
                tot += 31
        tot += b
        tot %= 7
        index = week_lst.index('FRI')
        index += tot
        if index >6:
            index -= 7
        weekday = week_lst[index]
        return weekday
    week(5, 24)
out : 
	'TUE'    
```

```python
in : 
    def solution(a, b):
        answer = ['FRI','SAT', 'SUN', 'MON', 'TUE','WEB','THU']
        month = [30, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 월별 날짜수

        if a > 1:
            for i in range(0, a-1):
                b = b + month[i]
        return answer[b % 7 -1]

	solution(1, 2)
out : 
'SAT'    
```



### 문제2

> 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

> 제한 조건: 공백은 아무리 밀어도 공백. s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있다. s의 길이는 8000이하이다. n은 1이상 25이하인 자연수이다.

```python
in : 
    # 여기에 코드를 작성하세요
    def siz(str_in, num_in):
        lst_si = []
        for i in str_in:
            if i != " ":
                lst_si.append(chr((ord(i)+num_in)))
        str_re = "".join(lst_si)
        return str_re

    siz('AB', 3)
out : 
    'DE'
```

```python
in : 
def solution(s, n):
    s = list(s)
    
    for i in range(len(s)):
        if s[i].isupper(): # 대문자인 경우
            s[i] = chr((ord(s[i])-ord('A') + n) % 26 + ord('A')) # GRAPE
        elif s[i].islower(): # 소문자인 경우
            s[i] = chr((ord(s[i])-ord('a') + n) % 26 + ord('a'))
    answer = "".join(s)
    return answer
out : 
	65 66
	C
```



### 문제3

> 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백 문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요

> 제한 사항: 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야 합니다.

```python
in : 
    # 여기에 코드를 작성하세요
    def updown(s):
        lst_s = s.split(" ")
        str_re = ""
        for i in lst_s:
            for j in i:
                if i.index(j) % 2 != 0:
                    str_re += j.upper()
                else:
                    str_re += j.lower()
            str_re += " "
        return str_re

    updown("Hi My Name Is")
out : 
	'hI mY nAmE iS '
```

```python
in : 
	def solution(s):
        word_list = []

        for word in s.split(" "):
            for i in range(0, len(word)): # i = 0
                word = word[:i] + (word[i].upper() if i % 2 == 0 else word[i].lower()) + word[i + 1]
            word_list.append(word)
        return " ".join(word_list)

    print(solution('cOffe'))
    print(solution('ricola candy'))
out : 
    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-44-e9289521b0dd> in <module>
          8     return " ".join(word_list)
          9 
    ---> 10 print(solution('cOffe'))
         11 print(solution('ricola candy'))

    <ipython-input-44-e9289521b0dd> in solution(s)
          4     for word in s.split(" "):
          5         for i in range(0, len(word)): # i = 0
    ----> 6             word = word[:i] + (word[i].upper() if i % 2 == 0 else word[i].lower()) + word[i + 1]
          7         word_list.append(word)
          8     return " ".join(word_list)

    IndexError: string index out of range
```



### 문제4

> 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각합니다, 첫째 줄에는 테스트 케이스의 개수 C가 주어지고, 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어집니다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수입니다. 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력하세요.

```python
in : 
    # 여기에 코드를 작성하세요
    c = 2
    ls_test_1 = [3, 30, 40, 50]
    ls_test_2 = [2, 60, 80]
    def test(ls_test):
        ave = sum(ls_test[1:])/ls_test[0]
        return ave
    ave1 = test(ls_test_1)
    ave2 = test(ls_test_2)
    count1, count2 = 0, 0
    for i in ls_test_1[1:]:
        if i > ave1:
            count1 += 1
    for i in ls_test_2[1:]:
        if i > ave2:
            count2 += 1
    print(ave1, round(count1/ls_test_1[0]*100, 3), "%")
    print(ave2, round(count2/ls_test_2[0]*100, 3), "%")
out : 
	40.0 33.333 %
	70.0 50.0 %
```

```python
in : 
    def ratio(t):
        for i in range(t):
            scores = list(map(int, input().split()))
            n = scores[0]
            scores = scores[1:]
            avg = sum(scores)/n
            cnt = len([s for s in scores if s > avg])
            print(avg, "%.3f" % (100*cnt/n), end='%\n')

    t = int(input("case"))

    print(ratio(t))
```



### 문제5

> 당신은 리스트의 요소중에서 처음으로 연속되지 않은 요소를 찾아야 합니다.예를 들어, [1, 2, 3, 4, 6, 7, 8] 이라는 리스트에서 1, 2, 3, 4는 모두 연속적이지만 6은 처음으로 연속되지 않은 요소입니다. 만약에 모든 리스트의 요소가 연속적이라면 null을 반환합니다. 배열에는 최소한 2개의 요소가 있어야 하고 모든 요소의 값은 숫자이며 중복은 없고 오름차순으로 정렬됩니다. 숫자는 음수 또는 양수 모두 가능합니다.

```python
in : 
    #여기에 코드를 작성하세요
    def con(lst):
        num = lst[0]
        for i in lst:
            if i == num:
                num += 1
            else:
                num = i
                break
        return num

    con([1, 2, 3, 4, 6, 7, 8])
out : 
    6
```



## 함수 문제 set 2



### 문제1

> 색이 칠해진 삼각형은 각각 빨강, 녹색 또는 파랑 색의 행에서 만들어집니다. 마지막 행보다 하나 적은 색을 각각 포함하는 연속 행은 이전 행에서 두 개의 색을 고려하여 생성됩니다. 이 색상이 동일하면 동일한 색상이 새 행에 사용됩니다. 색상이 다른 경우 누락 된 색상이 새 행에 사용됩니다. 단 하나의 색상으로 최종 행이 생성 될 때까지 계속됩니다.

> 삼각형의 첫 행을 문자열로 지정하고 마지막 행을 문자열로 표시하는 최종 색을 반환합니다. 위 예제의 경우 RRGBRGBB를 반환해야합니다. 입력 문자열에는 대문자 R, G, B 만 포함되며 적어도 하나의 문자가있어 유효하지 않은 입력을 테스트 할 필요가 없습니다. 한 색상 만 입력으로 받으면 해당 색상을 반환하십시오.

> 출력 결과
>
> - print(triangle('RRR')) => R
> - print(triangle('RG')) => B
> - print(triangle('RRRGGGBBBBBB')) => G
> - print(triangle('RRGBRGBB')) => G

> Adapted from the 2017 British Informatics Olympiad

```python
in : 
    #여기에 코드를 작성하세요
    def triangle(row):
        dicts = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}

        if len(row)> 2:
            s = ''
            for i in range(len(row)-1):
                s = s + dicts[row[i:i+2]]
            row = s
            return triangle(row)
        elif len(row) > 1:
            return dicts[row]
        else:
            return row
    print(triangle('RRR'))
out : 
    R
```

```python
in : 
    def triangle(row):
        if len(row) == 1:
            return row[0]

        colors = set(["B", "G", "R"])
        newrow = []
        for (l, r) in zip(row, row[1:]):
            if l == r:
                newrow.append(l)
            else:
                newrow.extend(colors - set([l, r]))

        return triangle(newrow)

    print(triangle('RRG'))
out : 
    G
```



### 문제2

> n개의 정수 리스트가 주어지면, 홀수와 짝수를 분리하고 각각의 조건에 맞게 홀수와 짝수를 정렬하세요.

> 조건
>
> 1. 짝수가 홀수보다 먼저오는 리스트를 반환합니다.
> 2. 짝수는 오름차순으로 홀수는 내림차순으로 정렬합니다.
> 3. 리스트의 크기는 적어도 4이상이어야 합니다.
> 4. 리스트의 요소값으로 0은 존재하지 않습니다.
> 5. 리스트의 요소값이 반복될 수 있으나 중복은 분리할 때 포함하지 않습니다.

> 출력결과
>
> - even_and_odd[7, 3 , 14 , 17] --> return [14, 17, 7, 3] :14는 짝수이기 때문에 가장 먼저 나오고 홀수는 내림차순으로 정렬을 하기 때문에 17, 7, 3 의 순서로 반환됩니다.

```python
in : 
    # 여기에 코드를 작성하세요
    def even_and_odd(lst):
        even_lst = []
        odd_lst = []
        for i in lst:
            if i % 2 == 0:
                even_lst.append(i)
            else:
                odd_lst.append(i)
        even_lst.sort()
        odd_lst.reverse()
        even_lst.extend(odd_lst)
        return even_lst

    print(even_and_odd([7, 3 , 14 , 17]))
out : 
    [14, 17, 3, 7]
```

```python
in : 
    def even_and_odd(arr):
        even = []
        odd = []
        for i in sorted(set(arr)): # set 자료형은 중복을 허용하지 않음
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd[::-1]

    print(even_and_odd([14, 17, 2, 7, 20, 3, 6, 13]))
out : 
    [2, 6, 14, 20, 17, 13, 7, 3]
```



### 문제3

> 정수로 된 리스트를 매개 변수로 가져와 해당 리스트의 모든 숫자를 처리할 수 있는 함수를 작성하세요. 처리 조건은 다음과 같습니다.숫자에 정수 제곱근이 있는 경우 제곱근을 해주고 그렇지 않으면 숫자를 제곱합니다.입력 리스트는 수정할 수 없습니다.

```python
in : 
    #여기에 코드를 작성하세요
    def rout(num_lst):
        result_lst = []
        for i in num_lst:
            if (i**0.5) % 1 == 0:
                result_lst.append(int(i**0.5))
            else:
                result_lst.append(i**2)
        return result_lst

    print(rout([1, 2, 3, 4, 9]))
out : 
    [1, 4, 9, 2, 3]
```



### 문제4

> 원하는 행까지 아래의 패턴을 생성하는 함수를 작성하세요. 만약 인자가 0이나 음의 정수인 경우 "" 즉, 빈 문자열로 반환하세요.짝수가 인수로 전달되면 패턴은 통과된 짝수보다 작은 최대 홀수까지 계속되어야 합니다.
>
> ```python
> # 예시 
> # pattern(9):
> 
> # 1
> # 333
> # 55555
> # 7777777
> # 999999999
> 
> # pattern(6)
> # 1
> # 333
> # 55555
> 
> # 유의
> # 패턴에 공백은 없습니다.
> ```
>
>

```python
in : 
    # 여기에 코드를 작성하세요
    def pattern(num):
        for i in range(1, num+1):
            if i % 2 != 0:
                print(f'{i}'*i)
            else:
                pass
        return ""

    print(pattern(9))
out : 
    1
    333
    55555
    7777777
    999999999
```

```python
in : 
    def pattern(n):
        string = ""
        a = n

        if a % 2 == 0:
            a -= 1
        for x in range (1, a + 1):
            if x % 2 != 0: # 홀수
                string += str(x) * x

                if x != a:
                    string += "\n"
        return string

    print(pattern(9))
out : 
    1
    333
    55555
    7777777
    999999999
```



### 문제5

> (QWERTY 키보드를 사용하여 타이핑을 한다고 가정할 때) '편안한 단어'는 타이핑 할 때 손을 번갈아 칠 수 있는 단어를 말합니다.단어를 인자로 받아 그것이 '편안한 단어'인지 여부를 True/False로 반환하는 함수를 만드세요.(모든 단어는 a ~ z까지 오름차순으로 구성된 문자열입니다.)

> 문자 목록
>
> - 왼손: q, w, e, r, t, a, s, s, d, f, g, z, x, c, v, b
> - 오른손: y, u, i, o, p, h, j, k, l, n, m

```python
in : 
    #여기에 코드를 작성하세요
    def soft(s):
        left_lst = ['q', 'w', 'e', 'r', 't', 'a', 's', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
        right_lst = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']

        for i in range(len(s)):
            if s[0] in left_lst:
                if (i % 2 == 0 and s[i] in left_lst) or (i % 2 != 0 and s[i] in right_lst):
                    pass
                else:
                    return False
            elif s[0] in right_lst:
                if (i % 2 == 0 and s[i] in right_lst) or (i % 2 != 0 and s[i] in left_lst):
                    pass
                else:
                    return False
        return True
    print(soft('amsld'))
out : 
    True
```

```python
in : 
    def confortable_word(word): # qywu
        left, right = "qwertasdfgzxcvb", "yuiophjklnm"
        l = True if word[0] in left else False # l true

        for letter in word[1:]: # ywu
            if letter in left and l:
                return False
            if letter in right and not l:
                return False
            l = not l # False
        return True

    print(confortable_word("qywu"))
    print(confortable_word("apple"))
out : 
    True
    False
```





