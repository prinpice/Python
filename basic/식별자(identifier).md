# 식별자(identifier)

변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름

## 특징

* 식별자의 이름은 영문알파벳, `_`, 숫자로 구성됨

* 첫 글자에 숫자가 올 수 없음

* 대소문자를 구별함

* 아래의 예약어(keyword)는 사용불가

  ```python
  False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
  ```

  * keyword 리스트 출력

    ```python
    in : 
        import keyword
        print(keyword.kwlist)
    out : 
        ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    ```

    

* 내장함수 또는 모듈 등의 이름 사용 불가

  * 내장함수 : 내부에 built-in 되어있는 함수

    ```python
    ex)
     str : 숫자를 문자로 바꿔주는 내장함수
     
     in : 
            str(5) # 숫자
     out : 
        	5 # 문자
    ```

  내장함수 또는 모듈 등의 이름을 식별자로 선언할 경우 해당 기능이 없어져서 사용불가

  ```python
  in : 
      # str() 형변환 함수로 정해진 식별자를 변수로 할당하면, 함수호출 불가
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

  