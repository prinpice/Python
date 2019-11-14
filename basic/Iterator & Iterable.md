# Iterator & Iterable

## Iterable

### Iterable Object

* 반복 가능한 객체
* `list`, `dict`, `set`, `str`, `bytes`m `tuple`, `range`



## Iterator

### Iterator Object

* 값을 차례대로 꺼낼 수 있는 객체

* iterable한 객체를 내장함수 또는 iterable 객체의 메소드로 객체 생성 가능

* `iter()` 또는 magic method인 `__iter__()`를 사용하여 iterator 생성

  ```python
  in :
      a = [1, 2, 3]
      a_iter = iter(a)
      print(type(a_iter))
  out :
      <class 'list_iterator'>
  ```

  ```python
  in :
      b = {1, 2, 3}
      b_iter = b.__iter__()
      print(type(b_iter))
  out :
      <class 'set_iterator'>
  ```



## Iterable에 유용한 내장함수

* `next(iterable)` : 해당 위치의 값을 꺼내고 다음으로 커서 이동

  ```python
  in :
      print(next(a_iter))
      print(next(a_iter))
      print(next(a_iter))
  out :
      1
      2
      3
  ```
  
* `all(iterable)` : 인수의 원소가 모두 참이면 True를 반환함(and와 같음)

  ```python
  in :
      print(all([1, 2, 3]))
      print(all([0, 1, 2, 3]))
  out :
      True
      False # 0은 False, 0을 제외한 모든 수는 True
  ```

* `any(iterable)` : 모두 거짓일 때 False를 반환함(or과 같음)

  ```python
  in :
      print(any([False, 3]))
      print(any([False, 0, []]))
  out :
      True
      False # empty list도 False에 해당됨
  ```

* `zip(*iterable)` : 동일한 개수로 이루어진 자료형을 묶어서 iterator로 반환함

  ```python
  in :
      a = zip([1, 2, 3], (4, 5, 6))
      print(next(a))
      print(next(a))
      print(next(a))
  out :
      (1, 4)
      (2, 5)
      (3, 6)
  ```

  * 두 개의 iterable 객체를 묶어 for문을 한꺼번에 반복시킬 때 유용함

  ```python
  in :
      country = ['대한민국', '스웨덴', '미국']
      capital = ['서울', '스톡홀롬', '워싱턴']
      for coun, cap in zip(country, capital):
          print(f'국가명 : {coun}, 수도 : {cap})
  out :
      국가명 : 대한민국, 수도 : 서울
      국가명 : 스웨덴, 수도 : 스톡홀롬
      국가명 : 미국, 수도 : 워싱턴
  ```

  

## itertools

* 반복가능한 데이터 스트림을 처리하는데 유용한 많은 함수와 generator가 포함되어 있음

* REPL을 통해 확인

* `count(시작, [step])` : 시작 숫자부터 step(없으면 1)만큼씩 무한히 증가하는 generator

* `islice(iterable객체, [시작], 정지[,step])` : iterable한 객체를 특정 범위로 슬라이싱하고 iterator로 반환함

  ```python
  # 소수를 구하는 함수
  def is_prime(x):
      if x > 1:
          for i in range(2, x):
              if x % i == 0:
                  return False
      else:
          return False
     	return True
  
  in :
      print(is_prime(5))
      print(is_prime(8))
  out :
      True
      False
  ```

  ```python
  # 0부터 999까지의 수 중에 소수인 수를 반환하는 iterator
  in :
      from itertools import islice, count
      thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
      print(next(thousand_primes))
      print(next(thousand_primes))
      print(next(thousand_primes))
  out :
      2
      3
      5
  ```

* `chain(*iterable)` : iterable한 객체들을 인수로 받아 하나의 iterator로 반환

  ```python
  in :
      from itertools import chain
      country = ['대한민국', '스웨덴', '미국']
      capital = ['서울', '스톡홀름', '워싱턴']
      c = chain(country, capital)
      print(next(c))
      print(next(c))
      print(next(c))
      print(next(c))
      print(next(c))
      print(next(c))
  out :
      '대한민국'
      '스웨덴
      '미국'
      '서울'
      '스톡홀름'
      '워싱턴'
  ```

  