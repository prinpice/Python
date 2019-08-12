# while03

```python
msg = " ***** 코리아 ATM *****\n"
msg += "1. 입금\n"
msg += "2. 출금\n"
msg += "3. 조회\n"
msg += "4. 종료\n"
my_money = 50000
atm_money = 1000
my_password = "12345"
"""
print(msg)
sel = int(input("번호를 입력하세요 >>> "))
if sel == 1:
    pass
elif sel == 2:
    pass
elif sel == 3:
    pass
"""
# 조건 입금 출금 조회 할때 마다 비밀번호 체크
# 입금 ==> 무한입금방지 (예외처리)
# 출금 ==> 마이너스 방지 (예외처리) (수수료 50원)
end = 0
while end == 0:
    print(msg)
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        password = input("비밀번호를 입력하세요 >>> ")
        if password == my_password:
            money_in = int(input("입금하실 금액을 입력하세요 >>> "))
            if my_money >= money_in:
                atm_money += money_in
                my_money = my_money - money_in
                print("통장 잔액은 ", atm_money, "원 입니다.")
                print("현 잔액은 ", my_money, "원 입니다.\n")
            else:
                print("금액이 부족합니다. 처음으로 돌아갑니다.\n")
        else:
            print("잘못 입력하셨습니다. 처음으로 둘아갑니다.\n")
    elif sel == 2:
        password = input("비밀번호를 입력하세요 >>> ")
        if password == my_password:
            money_out = int(input("출금하실 금액을 입력하세요(수수료 50원) >>> "))
            if money_out + 50 <= atm_money:
                atm_money = atm_money - money_out - 50
                my_money += money_out
                print("수수료는 50원 입니다.")
                print("통장 잔액은 ", atm_money, "원 입니다.")
                print("현 잔액은 ", my_money, "원 입니다.\n")
            else:
                print("잔액이 부족합니다. 처음으로 돌아갑니다.\n")
        else:
            print("잘못 입력하셨습니다. 처음으로 돌아갑니다\n")
    elif sel == 3:
        password = input("비밀번호를 입력하세요 >>> ")
        if password == my_password:
            print("통장 잔액은 ", atm_money, "원 입니다.")
            print("현 잔액은 ", my_money, "원 입니다.\n")
        else:
            print("잘못 입력하셨습니다. 처음으로 돌아갑니다.\n")
    elif sel == 4:
        print("종료합니다.")
        end = 1
    else:
        print("잘못 입력하셨습니다. 처음으로 돌아갑니다.\n")


#=====================================================================
# 반복문 ==> 1) 원하는 회수만큼 반복, 2) 짝수 홀수 출력, 3) 합출력, 4) 원하는 때에 종료
"""
total = 0
num = 0
while num <= 0:
    total = total +num
    num = num + 1
print("토탈 : ", total)
"""
```

