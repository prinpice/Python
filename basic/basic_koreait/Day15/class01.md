# class01

```python
# 클래스 ==> 내가만든 자료형 ==> (변수 + 함수)
"""
정의 방법 :
class + 이름: # 소괄호(함수) 없음
    (멤버변수) (멤버함수)
객체생성방법:
    변수 = 클래스명 + ()
사용방법:
    변수 + (.) + 내부변수 or 내부함수
"""
class Person: # (설계도)
    name = ""
    age = 0
    score = 0
    def show_info(self):
        print(self.name, self.age, self.score)

p1 = Person()
p1.name = "김철수"
p1.age = 20
p1.score = 80
p1.show_info() # 김철수 20 80

p2 = Person()
p2.name = "이영희"
p2.age = 30
p2.score = 50

print(p1.name, p1.age, p1.score) # 김철수 20 80
print(p2.name, p2.age, p2.score) # 이영희 30 50

lst = ["김철수", 20, 80] # 유사
print(lst)
```

