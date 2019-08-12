# while02

```python
msg = "***** 코리아 반점 *****\n"
msg += "1. 짜장면 7000원\n"
msg += "2. 짬뽕 8000원\n"
msg += "3. 탕수육 12000원\n"
msg += "4. 주문완료\n"
money = 50000
end = 0
#==============================================================
"""
print(msg)
sel = int(input("번호를 입력하세요 >>> "))
if sel == 1:
    pass
elif sel == 2:
    pass
elif sel == 3:
    pass
elif sel == 4:
    end = 1
"""

num = 0
while money > 7000 and end == 0:
    print(msg)
    print("현재 잔액은 ", money, "원 입니다.")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        num += 1
        if num <= 3:
            print("짜장면이 주문되었습니다.")
            money = money - 7000
            print("잔액은 ", money, "원 입니다.")
        else:
            print("짜장면이 매진되었습니다. 죄송합니다.")
    elif sel == 2:
        print("짬뽕이 주문되었습니다.")
        money = money - 8000
        print("잔액은 ", money, "원 입니다.")
    elif sel == 3:
        print("탕수육이 주문되었습니다.")
        money = money - 12000
        print("잔액은 ", money, "원 입니다.")
    elif sel == 4:
        print("종료합니다.")
        end = 1
    else:
        print("잘못 입력하셨습니다.")
    if money < 7000:
        print("잔액이 부족합니다.\n 종료합니다")

# 조건 1) 돈이 7000원 미만이면 종료
# 조건 2) 짜장면은 3그릇밖에 남지 않았다.

num = 0
while num <=10:
    if num % 2 == 0:
        print("짝수 :", num)
    num += 1
```

