# random

* 난수(random number)를 사용하기 위해 제공되는 module

```python
import random
```



## Method

* choice() : 배열에서 랜덤으로 하나의 값을 추출

  ```python
  random.choice([배열])
  ```

* randint() : 두개의 input 값 사이의 값들 중 임의의 정수를 반환함

  ```python
  random.randint([최소], [최대])
  ```

* random() : 0부터 1 사이의 부동소수점(float) 숫자를 반환함

  ```python
  random.random()
  ```

* randrange() : 두 개의 input 사이의 값들(지정된 간격으로 나열됨) 중 임의의 정수를 반환함

  ```python
  random.randrange([최소], [최대], [간격])
  ```

* sample() : 비복원 무작위 표본 추출

  ```python
  random.sample([리스트], [개수])
  ```

  * [리스트] : 나열 가능한 것들을 넣을 수 있음
  * [개수] : 선택하는 개수

* uniform() : 두 개의 input 값 사이의 값들 중 임의의 부동소수점(float) 숫자를 반환함

  ```python
  random.uniform([최소], [최대])
  ```

  

  

  