# test01

```python
# 복습
arr = [50, -10, 0, 30, 1, 6]
# 문제 1) 인덱스 입력받고 값 출력
# 문제 2) 값을 입력받고 인덱스 출력
names = ["kkk", "ppp", "ttt", "aaa"]
scores = [100, 20, 60, 40]
# 문제 1) 이름을 입력받고 점수 출력
# 문제 2) 점수를 입력받고 이름 출력
# 문제 3) 가장 점수가 높은 학생 이름 출력
max = scores[0]
num = 0
index = 0
while num < len(scores):
    if max < scores[num]:
        max = scores[num]
        index = num
    num += 1
print(names[index])



# ========================================================
# 반복문
# 0 ~ 10 사이의 숫자 출력
# 0 ~ 10 사이의 짝수 출력
# 0 ~ 10 합을 출력


# ========================= 심화 =========================
slide = ["읏", 10, 20 , 30 ,40 ,50 , 60]
# 문제 1) d 를 입력받으면 "읏" 이 오른쪽으로 이동 a 는 왼쪽 이동
end = 0
temp = None
num2 = 0
while end == 0:
    num1 = 0
    print(slide)
    al = input("a 또는 d 를 입력하시오(a는 왼쪽 이동, d는 오른쪽 이동, 종료: e) >>> ")
    while num1 < len(slide):
        if slide[num1] == "읏":
            num2 = num1
        num1 += 1
    if al == "a":
        if num2 == 0:
            temp = slide[0]
            slide[0] = slide[6]
            slide[6] = temp
        else:
            temp = slide[num2]
            slide[num2] = slide[num2 - 1]
            slide[num2 - 1] = temp
    elif al == "d":
        if num2 == 6:
            temp =slide[6]
            slide[6] = slide[0]
            slide[0] = temp
        else:
            temp = slide[num2]
            slide[num2] = slide[num2 + 1]
            slide[num2 + 1] = temp
    elif al == "e":
        end = 1
```

