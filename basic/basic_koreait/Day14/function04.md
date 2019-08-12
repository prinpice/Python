# function04

```python
myMoney = 1000

def addMoney(myMoney):
    inputM = int(input("입금할 금액을 입력하세요 >> "))
    myMoney += inputM
    return myMoney

while True: # True 로 하면 항상 무한반복으로 된다. (beak)로 종료시키면 된다.
    print("atm")
    print("1. 입금")
    sel = int(input("번호를 입금하세요 >> "))
    if sel == 1:
        myMoney = addMoney(myMoney)
        print((myMoney))
    else:
        break
```

