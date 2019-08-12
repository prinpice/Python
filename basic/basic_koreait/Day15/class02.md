# class02

```python
# 클래스 내부함수에서 내부변수를 사용할때는 반드시 self 를 붙여줘야한다.
class TV:
    brand = ""   # 구성위한예시도구
    size = 0     # 구성위한예시도구
    channel = 0  # 구성위한예시도구
    def set_info(self, b, s):
        self.brand = b
        self.size = s

    def show_info(self):
        print(self.brand, self.size, self.channel)
    def channel_up(self):
        self.channel += 1
    def channel_down(self):
        self.channel -= 1
    def show_channel(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        if self.channel == 1:
            print("드라마")
        elif self.channel == 2:
            print("영화")
        elif self.channel == 3:
            print("스포츠")
        else:
            print("치지직")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
    def show_menu(self):
        while True:
            print("TV_MENU")
            print("1. 채널 업")
            print("2. 채널 다운")
            print("3. 종료")
            sel = int(input("번호를 입력하세요 >> "))
            if sel == 1:
                self.channel_up()
                self.show_channel()
            elif sel == 2:
                self.channel_down()
                self.show_channel()
            elif sel == 3:
                break
"""
tv1 =TV()
tv1.brand = "LG"
tv1.size = 40
tv1.show_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

tv2 =TV()
tv2.brand = "삼성"
tv2.size = 50
tv2.show_info()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

lst = ["삼성", 50, 0]
lst2 = ["LG", 40, 0]
print(lst)
print(lst2)

tv3 = TV()
tv3.set_info("애플", 60)
tv3.show_info()
"""
```

