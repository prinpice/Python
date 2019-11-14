# os

* 기타 운영 체제 인터페이스

```python
import os
```



## Method

* listdir() : 지정된 디렉토리 전체 목록 얻기                                                                                                                                                                        

  ```python
  os.listdir('[폴더주소]')
  ```

  ```python
  os.listdir('.') # 현재 위치의 목록
  ```

* chdir() : 특정 경로로 이동

  ```python
  os.chdir("[경로]")
  ```

* getcwd() : 현재 위치 주소 출력

  ```python
  os.getcwd()
  ```

* rename() : 파일명 수정

  ```python
  os.rename(filename, filename.replace("aa", "bb"))
  ```

  

