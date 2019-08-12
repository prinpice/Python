# game

```python
# 숫자 야구 게임
BB = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 0~9 사이의 값을 ai me 하나씩 선택한다 둘다 중복 선택 불가
strike = 0
ball = 0
# 문제 1) BB를 셔플한다, 후 com 앞에서 순서대로 3개만 저장한다.
# 예) 1, 5, 3
# me 는 숫자 3개를 입력받아서 저장한다.
# com 과 me 안의 숫자를 같은숫자가 있는지 비교한다.
# 자리와 숫자가 같으면 shrike += 1, 숫자만 같으면 ball += 1
# 위정보를 토대로 strike 3을 만들 때까지 반복
# 예) com = [1, 5, 3], me = [2, 1, 5] ==> 2b
# 예) com = [1, 5, 3], me = [1, 5, 7] ==> 2s
import random
while strike < 3:
    com = []
    me = []
    count = 0
    for i in range(10):
        num1 = random.randint(0,9)
        temp = BB[i]
        BB[i] = BB[num1]
        BB[num1] = temp
    com.append(BB[0])
    com.append(BB[1])
    com.append(BB[2])
    while count < 3:
        num2 = int(input("숫자를 입력하세요 >>"))
        if num2 >= 0 and num2 <= 9:
            me.append(num2)
            count += 1
        else:
            print("다시 입력하세요")
    for i in range(3):
         for j in range(3):
            if me[j] == com[i] and i == j:
                strike += 1
            if me [j] == com[i] and i != j :
                ball += 1
    print(com)
    print(me)
    print(strike, ball)
print("종료")


# 빙고
bingo =[0, 0, 0, 0, 0, 0, 0]
# 문제 1) 인덱스를 입력받으면 해당 값이 3으로 바뀜
# 예 ) 입력 ==> 1 ==> 0, 3, 0, 0, 0, 0, 0,
# 3이 연속 3줄이면 "빙고" 출력

# 리스트
lst = [10, 20, 30, 40, 50, 60]
# 문제 1) 인덱스를 입력받고 값 출력
# 문제 2) 값을 입력받고 인덱스 출력
```

