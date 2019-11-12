# 코드 라인(Code Line)

* python 에서는 기본적으로 `;`을 작성하지 않음

* 한 줄에 여러줄의 코드를 작성할 경우 `;`을 사용

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

* 코드를 여러줄에 걸쳐서 작성시에는 가독성을 높이기 위해 `\`를 사용함

  ```python
  in : 
      a = 0
  	if a\
  	== 0 : 
      	print(a) # 0
  ```

* `[]`, `{}`, `()`는 `\` 없이도 가능함

  * `[]` : list 자료형
  * `{}` : dictionary 자료형
  * `()` : tuple 자료형

  ```python
  in : 
      lunch = ["짜장면", "탕수육", 
           	"깐풍기"]
  ```

  