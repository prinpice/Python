# 형변환(Conversion)

* python에서 data type은 서로 변환 가능

## 암시적 형변환(Implicit Type Conversion)

* 사용자가 의도하지 않았지만, 파이썬 내부적으로 자동으로 형변환되는 경우

  * bool
  * Bumbers(int, float, complex)

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

* 암시적 형변환을 제외한 모든 경우
  * `string` -> `integer` : 형식에 맞는 숫자만 가능
  * `integer` -> `string` : 모두 가능
* 암시적 형변환이 가능한 경우
  * `int()` : `string`, `float`를 `int`로 변환
  * `float()` : `string`, `int`를 `float`로 변환
  * `str()` : `int`, `float`, `list`, `tuple`, `dictionary`를 문자열로 변환
  * `list()`
  * `tuple()`