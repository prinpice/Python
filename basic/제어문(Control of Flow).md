# 제어문(Control of Flow)

* 종류
  * 조건문
  * 반복문
* 순서도(Flow Chart)로 표현가능



## 조건문(if)

* 일정한 참/거짓을 판단할 수 있는 `조건식`과 **반드시** 함께 사용되어야 함

  `if <조건식>:`

  * `<조건식>`이 참인 경우 : `:` 이후의 문장을 수행
  * `<조건식>`이 거짓인 경우 : `else:` 이후의 문장을 수행

  ```python
  if dust > 50:
      print("50초과")
  else:
      print("50이하")
  ```

* **들여쓰기** 유의해야함

  * 파이썬에서는 코드 블럭을 java, c언어의 `{}`와 달리 **들여쓰기로 판단함**
  * 일반적으로 `PEP-8`에서 권장하는 `4spaces`를 사용함

* 2개 이상의 조건문을 활용할 경우 `elif <조건식>:`을 활용함

  ```python
  if dust > 150:
      print("매우나쁨")
  elif<조건식>:
      print("나쁨")
  elif<조건식>:
      print("보통")
  else:
      print("좋음")
  ```

### 조건표현식(Conditional Expression)

```python
true_value if <조건식> else false_value
```

* 다른 언어에서 활용되는 삼항연산자와 동일함

  ```python
  in :
      a = int(input("숫자를 입력하세요 : "))
  	print("3이 맞음") if a == 3 else print("3이 아님")
  out : 
      숫자를 입력하세요 : 3
  	3이 맞음
  ```

* 일반적으로 조건에 따라 값을 정할 때 많이 활용됨

  ```python
  in : 
      # 아래의 코드는 무엇을 위한 코드일까요? # input숫자가 0보다 크거나 같은경우 출력
      num = int(input("숫자를 입력하세요 : "))
      value = num if num >= 0 else 0
      print(value)
  out : 
      숫자를 입력하세요 : 5
  5
  ```

  ```python
  in : 
      # 다음의 코드와 동일한 조건 표현식을 작성해보세요.
      num = 2
      if num % 2:
          result = '홀수입니다.'
      else:
          result = '짝수입니다.'
      print(result)
  out : 
      짝수입니다.
  ```

  ```python
  in : 
      num = 2
  	print("홀수입니다.") if num % 2 else print("짝수입니다.")
  out : 
      짝수입니다.
  ```

  

## 반복문(while, for)

### while

* 조건식이 True인 경우 반복적으로 코드를 실행함

* **종료조건**을 반드시 설정해주어야함

  ```python
  in : 
      a = 0
      while a < 5:
          print(a)
          a += 1
      print("끝")
  out : 
      0
      1
      2
      3
      4
      끝
  ```

* `<조건식>`dlgndp `:`이 반드시 필요하며, 이후에 오는 코드 블록은 `4spaces`로 **들여쓰기**해야 함

* infinite loop

  ```python
  while True:
      print("계속해주세요")
  ```

### for

* 정해진 범위 내(sequence)에서 순차적으로 코드를 실행

  ```python
  for i in sequence:
      print("정해진 범위 내에서 계속")
  ```

  ```python
  for variable in sequence:
      code line1
      code line2
  ```

  * `for`문은 `sequence`를 순차적으로 **variable**에 값을 바인딩하며, 코드 블록을 시행함

  ```python
  dust = [59, 24, 102]
  for i in dust:
      print(i)
  ```

* **enumerate()**

  * 파이썬 표준 라이브러리의 내장함수
  * 열거 객체를 반환함

  ```python
  in : 
      lunch = ["짜장면", "초밥"]
  	for idx, menu in enumerate(lunch):
      	print(idx, menu)
  out : 
      0 짜장면
  	1 초밥
  ```

  ```python
  in : 
      classroom = ["kim", "choi", "lee"]
  	list(enumerate(classroom,start=0))
  out : 
      [(0, 'kim'), (1, 'choi'), (2, 'lee')]
  ```

  ```python
  in : 
      classroom = ["kim", "choi", "lee"]
  	list(enumerate(classroom,start=1))
  out : 
      [(1, 'kim'), (2, 'choi'), (3, 'lee')]
  ```

* dictionary 사용하기

  * dictionary의 `key`를 출력함으로서 `value`에도 접근 가능함

  ```python
  in : 
      classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
      for member in classroom:
          print(member)
  out : 
      teacher
      student1
      student2
  ```

  ```python
  in : 
      classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
      classroom["teacher"]
  out : 
      'Kim'
  ```

  * 활용방법(4가지)

    ```python
    # 0. dictionary (key 반복)
    for key in dict:
        print(key)
    
    # 1. key 반복
    for key in dict.keys():
        print(key)
    
    # 2. value 반복    
    for val in dict.values():
        print(val)
    
    # 3. key와 value 반복
    for key, val in dict.items():
        print(key, val)
    ```



### break, continue, else

#### `break`

* 반복문을 종료하는 표현

  ```python
  in : 
      for i in range(10):
  	    if i != 0:
      	    break
      	print(i)
  out : 
      0
  ```

#### continue

* `continue` 이후의 코드를 수행하지 않고, 다음 요소를 선택해 반복을 계속 수행함

  ```python
  in : 
      for i in range(6):
  	    if i % 2 == 0:
      	    continue
          	print(f'{i}는 홀수')	
  out : 
      # 없음
  ```

  ```python
  in : 
      for i in range(6):
  	    if i % 2 == 0:
      	    continue
          	print(f'{i}는 홀수')	
  out : 
      1는 홀수
      3는 홀수
      5는 홀수
  ```

#### else

* 끝까지 반복문을 시행하 이후에 실행됨(break를 통해 중간에 종료되지 않은 경우만 실행)

  ```python
  in : 
      for i in range(3):
          if i == 3:
              print(f'{i}에서 break')
              break
          else:
              print("break 시행안됨")
  out : 
      break 시행안됨
      break 시행안됨
      break 시행안됨
      # 범위가 0~2이기 때문에 i != 3
  ```

  ```python
  in : 
      for i in range(4):
          if i == 3:
              print(f'{i}에서 break')
              break
          else:
              print("break 시행안됨")
  out : 
      break 시행안됨
      break 시행안됨
      break 시행안됨
      3에서 break
  ```

  