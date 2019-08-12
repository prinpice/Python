# list02

```python
# 리스트의 슬라이싱 및 인덱싱
#
lst = [1, 2, 3, [4, 5, 6]]
# 문제 1) 5를 출력해보세요
print(lst[0]) #
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[3][0])
print(lst[3][1]) #5

# 슬라이싱
lst = [1, 2, 3, 4, 5, 6]
print(lst[2:4]) # [3, 4]

lst = [1, 2, 3, ["a", "b", "c"], 4, 5]
# 문제 1 ) [b, c]
print(lst[3][1:3])

name = ["김철수", "김만수", "김영희", "이정수", "이철"]
score = [100, 20, 30, 60, 80]

# 문제 1)이름을 입력받고 해당 점수를 출력
num1 = 0
name1 = input("이름을 입력하세요: ")
while num1 < 5:
    if name1 == name[num1]:
         print("점수: ", score[num1])
    num1 += 1

# 문제 2) 점수를 입력받고 학생이름 출력
num1 = 0
score1 = int(input("점수를 입력하세요: "))
while num1 < 5:
    if score1 == score[num1]:
        print("해당 점수 학새 이름: ", name[num1])
    num1 += 1
# 문제 3) 이름 2개를 입력받고 해당 학생의 점수 교환
name1 = input("이름1을 입력하세요: ")
name2 = input("이름2를 입력하세요: ")
num1 = 0
score1 = 0
score2 = 0
while num1 < 5:
    if name1 == name[num1]:
        score1 = score[num1]
    elif name2 == name[num1]:
        score2 = score[num1]
    num1 += 1
score3 = score1
score1 = score2
score2 = score3
print(name1, "의 점수: ", score1, ", ", name2, "의 점수: ", score2)
# 문제 4) 가장 점수가 높은 학생 이름 출력
max1 = score[0]
num1 = 0
while num1 < 5:
    if max1 < score[num1]:
        max1 = score[num1]
    num1 += 1
num2 = 0
while num2 < 5:
    if max1 == score[num2]:
        print("가장 점수가 높은 학생 이름: ", name[num2])
    num2 += 1

```

