# while02

```python
import random
num = random.randint(0, 100)
# print("랜덤숫자 : ", num)
# 게임 업다운게임
#  조건 1) ai 는 랜덤 0 ~ 100 사이의 숫자를 저장한다.
#  조건 2) me 는 0 ~ 100 사이의 숫자를 입력한다. (여기서부터 반복)
#  조건 3) ai 와 me 를 비교후 결과 출력 (크다 작다 같다)
#  조건 4) 위의 정모를 토대로 맞출떄까지 반복 (반복횟수 count) 출력
#  조건 5) 맞추면 종료

# ai = None # if 문에서 pass 와 같이 변수도 미리 만들어놓을 수 있다. None 를 사용한다.
ai = num
me = None
count = 0
while ai != me:
    me = int(input("0 ~ 100 사이의 숫자를 입력하시오 >>> "))
    if me > ai:
        print("크다")
    elif me < ai:
        print("작다")
    else:
        print("같다")
        print("종료")
    count += 1
    print("반복횟수 :", count)

# 동전 앞(0) 뒤(1) 게임
# 조건 1) ai 는 랜덤으로 0 , 1 을 저장한다.
# 조건 2) me 는 0 , 1  을 입력한다.
# 조건 3) ai 와 me 를 비교 후 결과 출력

```

