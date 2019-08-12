# class02

```python
class TV:
    def set_info(self, b, s, p):
        self.brand = b
        self.size = s
        self.price = p
    def show_inf0(self):
        print(self.brand, self.size, self.price)

class Radio: pass
class Computer: pass

HIMART = []
JANG = []
TV_all = []

t1 = TV()
t1.set_info("LG", 3, 150)
TV_all.append(t1)
t1.set_info("Samsung", 5, 300)
TV_all.append(t1)
t1.set_info("LG", 5, 200)
TV_all.append(t1)
t1.set_info("Samsung", 3, 200)
TV_all.append(t1)

print(TV_all)

while True:

    print("하이마트")
    print("1. 상품목록")
    print("2. 장바구니")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 1:
        for i in HIMART:
            print(i)

        sel = int(input("번호를 입력하세요 >> "))
```

