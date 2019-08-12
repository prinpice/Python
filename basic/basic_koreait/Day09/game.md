# game

```python
# 배달게임
import random
x, y, speed, des_x, des_y = 0, 0, 0, 10, -5
count = 0 # 3 개만
end = 0
direction = 0 # 0, 1, 2, 3 ==> 동서남북
while end == 0:
    print("*****배달게임*****")
    print("목적지 : des_x :", des_x, ", des_y :", des_y)
    print("현재위치 x : ", x, ", y : ", y, ", 방향(0: 동, 1: 서, 2: 남, 3: 북", direction, ", 속도 :", speed)
    print("짐 : ", count)
    print("1. 속도")
    print("2. 전진")
    print("3. 좌회전")
    print("4. 우회전")
    print("5. 종료")
    print("==============================")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        speed = int(input("속도를 입력하세요 (0~3) >>> "))
        if speed < 0 or speed > 3:
            print("잘못 입력하셨습니다.")
            speed = 0
    if sel == 2:
        if direction == 0:
            x += speed
        elif direction == 1:
            x -= speed
        elif direction == 2:
            y -= speed
        elif direction == 3:
            y += speed
    if sel == 3:
        if direction == 0:
            direction = 3
        elif direction == 1:
            direction = 2
        elif direction == 2:
            direction = 0
        elif direction == 3:
            direction = 1
    if sel == 4:
        if direction == 0:
            direction = 2
        elif direction == 1:
            direction = 3
        elif direction == 2:
            direction = 1
        elif direction == 3:
            direction = 0
    if sel == 5:
        end = 1
    if x == des_x and y == des_y:
        print("목적지에 도착했습니다. 새로운 목적지를 설정합니다.")
        count += 1
        des_x = random.randint(-10, 10)
        des_y = random.randint(-10, 10)
    if count >=3:
        end = 1 # ("미션 성공")
print("종료")
# 문제 1) 스피드는 3을 넘을 수 없다.
# 문제 2) 목적지에 도착하면 랜덤으로 다음 목적지 설정 -10 ~ 10
# 응용문제 3) 동서남북 구현
```

