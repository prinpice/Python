# class01

```python
# 어차피 클래스 내부 변수 (self 변수) 들은 초기화를 해야한다.
# 그래서 클래스를 만들때 자동으로 호출해주는 함수가 있다.(__init__)

class Car:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.dir = 0 # 자동으로 실행됨
    """
    def init(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.dir = 0
    """ # 직접 불렀을때만 실행됨
    def speed_up(self):
        pass
    def go_forward(self):
        pass
    def left_turn(self):
        pass
    def right_turn(self):
        pass
    def show_pos(self):
        print(self.x, self.y, self.speed, self.dir)
    def controller(self):
        while True:
            print("배달게임")
            print("1. 속도\n2. 전진\n3. 좌회전\n4. 우회전\n5. 위치\n6. 종료")
            sel = int(input("번호를 입력하세요 >>> "))
            if sel == 6:
                break

c1 = Car()
c1.controller()
c2 = Car()
c2.controller()
```

