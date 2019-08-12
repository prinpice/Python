# function06

```python
pocketMoney = 1000 # 주머니에 있는돈

names = ["aaa", "bbb", "ccc", "ddd"]
pw = ["1234", "2345", "3456", "4567"]
account = ["111-111", "222-222", "333-333", "444-444"]
balance = [30200, 10000, 40000, 60000]
def account_c(account1, pw1):
    account2 = input("계좌를 입력하세요 >>> ")
    pw2 = input("비밀번호를 입력하세요 >>> ")
    num1 = 0
    while num1 < len(account):
        if account2 == account[num1] and pw2 == pw[num1]:
            num = num1
            return num
        num1 += 1
    return 0

def addMoney(pM, aM):
    check = account_c(account[num], pw[num])
    if check == 1:

    inputM = int(input("입금할 금액을 입력하세요 >> "))
    balance[num] += inputM # 주머니돈이 계좌로 간다.
    pM -= inputM # 계좌로 간 돈은 주머니돈에서 빼야된다.
    return pM, aM


while True:  # True 로 하면 항상 무한반복으로 된다. (beak)로 종료시키면 된다.
    print("atm")
    print("1. 입금")
    print("2. 송금")
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

ATN_DB = [["aaa", "1234", "111-111", 30200 ], ["bbb", "2345", "222-222", 10000]]
```

