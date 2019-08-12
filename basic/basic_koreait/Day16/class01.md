# class01

```python
class StudentManager: pass

class Student:
    def set_info(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def show_info(self):
        print("===============================")
        print(self.name, self.age, self.score)
        print("===============================")


s1 = Student()
s1.set_info("김철수", 20, 100)
# s1.name = "김철수"
# s1.age = 20
# s1.score = 100
s1.show_info()
# print(s1.score)
# print(s1.name)
# print(s1.age)
st_lst = []
st_lst.append(s1)

while True:
    print("학생 과리 프로그램")
    print("1. 등록")
    print("2. 삭제")
    print("3. 조회")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 1:
        name = input("이름?")
        age = int(input("나이?"))
        score = int(input("성적?"))
        temp = Student()
        temp.set_info(name, age, score)
        st_lst.append(temp)
    if sel == 3:
        for i in st_lst:
            i.show_info()
```

