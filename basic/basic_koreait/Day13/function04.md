# function04

```python
def check_pw(in_pw):
    in_pw = int(input("비밀번호를 입력하세요 >> "))
    if in_pw == my_pw:
        return 1 # 1 은 참 # 리턴키워드는 함수를 종료시킨다.
    return 0  # 0 은 거짓
def input1(atm_money , my_pw):
    check = check_pw(my_pw)
    if check == 1:
        input_m = int(input("입금할 금액을 입력하세요 >>> "))
        atm_money += atm_money + input_m
    else: print("비밀번호를 확인하세요 ")
    return atm_money
def output(): pass
my_pw = 1234
end = 0
my_money = 10000
atm_money = 1000
while end == 0:
    print("ATM")
    print("1. 입금\n2. 출금\n3. 조회\n4. 종료")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 4:
        break
    if sel == 1:
            atm_money = input(atm_money, my_pw)
    if sel == 2:
        in_pw = int(input("비밀번호를 입력하세요 >> "))
        if in_pw == my_pw:
            pass
    if sel == 3:
        in_pw = int(input("비밀번호를 입력하세요 >> "))
        if in_pw == my_pw:
            pass
"""        
while end == 0:
    print("ATM")
    print("1. 입금")
    print("2. 출금")
    print("3. 조회")
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >> "))
    if sel == 4:
        break
    if sel == 1:
        in_pw = int(input("비밀번호를 입력하세요 >> "))
        if in_pw == my_pw:
            pass
    if sel == 2:
        in_pw = int(input("비밀번호를 입력하세요 >> "))
        if in_pw == my_pw:
            pass
    if sel == 3:
        in_pw = int(input("비밀번호를 입력하세요 >> "))
        if in_pw == my_pw:
            pass
"""
```

