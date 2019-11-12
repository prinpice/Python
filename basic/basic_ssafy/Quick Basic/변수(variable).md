# 변수(variable)

* 변수는 박스(dust)와 같음

  * dust는 60이다 (x) / dust에 60을 저장한다(o)

* 변수는 `=`을 통해 할당(assignment)됨

  * `=` : 할당문 연산자

* `type()`으로 해당 자료형 확인 가능

* `id()` 로 해당 변수의 메모리 주소 확인 가능

  * 변수에 값이 저장되는 것(x) / 값에 해당하는 주소를 저장(o)

  ```python
  in : 
      x = 1004
      print(x) # 1004
      print(id(x)) # 91060160
      type(x)
  out : 
      int
  ```

* 동일한 값을 동시에 할당 가능

  ```python
  in : 
      w = t = 1004
      print(w, t) # 1004 1004
  ```

* 다른 값을 동시에 할당 가능

  ```python
  in : 
  	x, y = 1, 2
  	print(x, y) # 1 2
  ```

* 값을 서로 바꿈

  ```python
  in : 
      # 쉽게 변수 값을 swap 가능함.
  	print(x, y) # 1 2
  	x, y = y, x
  	print(x, y) # 2 1
  ```

  