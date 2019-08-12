# class03

```python
# 방법 1
class StudentManager: pass
class Student:
    def set_info(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 방법 2
st_info = ["aaa", 20, 100]
st_info_manager = []
st_info_manager.append(st_info)

name = ["aaa", "bbb", "ccc"]
age = [10, 20, 25]
score = [100, 60, 57]
st_lst = []
# 방법 3
def show_info():pass
def add_info(): pass
def remove_info(): pass
"""
while True:
    print("학생관리프로그램\n1. 등록\n2. 삭제\n3. 조회\n4. 종료")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 1: show_info()
    elif sel == 2: remove_info()
    elif sel == 3: show_info()
    else: break
"""

while True:
    print("학생관리프로그램\n1. 등록\n2. 삭제\n3. 조회\n4. 종료")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 1:
        name1 = input("이름을 입력하세요 >> ")
        age1 = int(input("나이를 입력하세요 >> "))
        score1 = int(input("점수를 입력하세요 >> "))
        temp = Student()
        temp.set_info(name1, age1, score1)
        st_lst.append(temp)
        print(st_lst)
```

