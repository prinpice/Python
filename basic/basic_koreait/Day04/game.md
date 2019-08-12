# game

```python
import random # 랜덤숫자를 사용할 수 있다.

num = random.randint(0, 2) # 0, 1, 2 셋중에 하나가 랜덤으로 반환된다.
# print(random.randint(0, 2))
#print("num")

"""
# 홀짝 게임
# 조건 1) com 은 0~1의 랜덤숫자를 저장한다.
# 조건 2) me 에 0~1의 숫자를 입력받는다.
# 조건 3) com 의 숫자를 맞추면 "성공" 틀리면 "실패" 를 출력한다.
# 조건 4) money 에 1000 을 저장하고 com 의 숫자를 맞추면 500 증가 실패하면 500 감소 후 출력


com = random.randint(0, 1)
money = 1000
print("money =", money)
me = int(input("0 또는 1을 입력하시요 >>>"))
print("me =", me)
print("com =", com)
if me == com:
    print("성공")
    money1 = money + 500
    print("money =", money1)
else:
    print("실패")
    money2 = money - 500
    print("money =", money2)
"""
"""
print("*** 코리아 홍콩반점 ***")
print("1. 짜장면 : 6000원")
print("2. 짬뽕 : 7000원")
print("3. 탕수육 : 12000원")
select = int(input("번호를 입력하세요 >>> "))
money = 10000
# 거스름돈 주문한음식 등등 # 이상한번호 입력시 경고 메세지 등등...
print("money =", money)
if select == 1:
    print("주문한 음식 : 짜장면, 거스름돈 : 4000원")
elif select == 2:
    print("주문한 음식 : 짭뽕, 거스름돈 : 3000원")
elif select == 3:
    print("주문한 음식 : 탕수육, 잔액이 부족합니다.")
else:
    print("주문이 취소되었습니다.")
"""
"""
# 가위바위보게임
# 조건 1) com 은 0~2 의 랜덤숫자를 저장한다. 가위(0) 바위(1) 보(2)
# 조건 2) me 는 0~2 숫자를 입력받는다.
# 조건 3) 결과 출력 (이겼다 비겼다 졌다)


com = random.randint(0, 2)
me = int(input("0(가위), 1(바위), 2(보) 중 하나를 입력하세요>>> "))
print("com =", com)
print("me =", me)
if me == 0:
    if com == 2:
        print("이겼다")
    elif com == 1:
        print("졌다")
    else:
        print("비겼다")
elif me ==1:
    if com == 2:
        print("졌다")
    elif com == 1:
        print("비겼다")
    else:
        print("이겼다")
else:
    if com == 2:
        print("비겼다")
    elif com ==1:
        print("이겼다")
    else:
        print("졌다")
"""

# 게임의 최종목표 ==> 윷놀이
```

