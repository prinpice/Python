# test04

```python
import random
class CoinGame:
    coin = None  # 구성위한 예시(설계도구)
    def show_menu(self):
        coin = random.randint(0, 1)
        print("코인게임")
        self.sel = int(input("앞(0), 뒤(1) 를 입력하세요 >> "))
        if coin == 0:
            print("coin == 앞")
        else:
            print("coin == 뒤")
        if self.sel == self.coin:
            print("승리!")
        else:
            print("패배")
coin1 = CoinGame()
coin1.show_menu()
```

