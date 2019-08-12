# class03

```python
from Day15.class_15_02 import TV
from Day15.test_15_04 import CoinGame

"""
tv1 = TV()

tv1.set_info("삼성", 50)

# tv1.show_channel()
# tv1.channel_up()
# tv1.show_channel()
# tv1.channel_up()
# tv1.show_channel()
# tv1.channel_down()
# tv1.show_channel()

tv1.show_menu()

tv2 = TV()
tv2.show_info()
"""
while True:
    print("나만의 게임리스트")
    print("1. tv")
    print("2. 동전")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 1:
        tv1 = TV()
        tv1.show_menu()
    elif sel == 2:
        con1 =CoinGame()
        con1.show_menu()
    else:
        break
# 앞뒤 ==> 클래스 변경해서 활용해보자~
```

