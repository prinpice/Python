# function05

```python
pocketMoney = 1000 # 주머니에 있는돈
atmMoney = 4000 # 계좌에 있는돈
def addMoney(pM, aM):
    inputM = int(input("입금할 금액을 입력하세요 >> "))
    aM += inputM # 주머니돈이 계좌로 간다.
    pM -= inputM # 계좌로 간 돈은 주머니돈에서 빼야된다.
    return pM, aM


while True:  # True 로 하면 항상 무한반복으로 된다. (beak)로 종료시키면 된다.
    print("atm")
    print("1. 입금")
    sel = int(input("번호를 입금하세요 >> "))
    if sel == 1:
        returnData = addMoney(pocketMoney, atmMoney)
#        print(returnData)
        atmMoney = returnData[0]
        pocketMoney = returnData[1]
#        print(atmMoney, pocketMoney)
        print("pocketMoney: ", pocketMoney)
        print("atmMoney: ", atmMoney)
    else:
        break
```

