# deck

```python
from Day18.card_game.card import Card # 암포트 경로 설정


class Deck:
    def __into__(self): # 초기화
        self.deck = []
        for i in range(40):
            self.c1 = Card()
            self.temp = []
            self.temp.append(self.c1.card_shape[i % 4])
            self.temp.append(self.c1.card_num[i // 4])
            self.c1.shape = self.temp[0]
            self.c1.num = self.temp[1]
            self.deck.append(self.temp)
    def shuffle(self):
        import random
        for i in range(1000):
            self.ran = random.randint(0, 39)
            self.temp = self.deck[self.ran]
            self.deck[self.ran] = self.deck[0]
            self.deck[0] = self.temp
    def sort(self): # 원래대로 정렬
        pass
    def show_info(self):
        for i in range(40):
            print(self.deck[i].shape, self.deck[i].num, end="")
            if i % 4 == 3:
                print()
deck1 = Deck()
deck1.shuffle()
deck1.show_info()

# 문제 1) 셔플 함수를 구현해보세요
```

