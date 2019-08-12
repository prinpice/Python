# test02

```python
# 반복문 1) 0 ~ 10 사이의 합을 출력

lst = [11, 20, 60, 0 , 64, -7]
"""
# 리스트 1 ==> 인덱스를 입력받고 값 출력 ==> 0 ==> 11
index = int(input("인덱스를 입력하세요: "))
print(lst[index])
"""
"""
# 리스트 2 ==> 값을 입력받고 인덱스 출력 ==> 64 ==> 4
num1 = int(input("값을 입력하세요: "))
index = 0
while index < len(lst):
    if num1 == lst[index]:
        print("인덱스: ", index)
    index += 1
"""
"""
# 리스트 3 ==> 가장큰값 찾기 ==> 64
max1 =lst[0]
num1 = 0
while num1 < len(lst):
    if max1 < lst[num1]:
        max1 = lst[num1]
    num1 += 1
print("가장 큰 값: ", max1)
"""
# ==========================================================
name = ["김철수", "김만수", "김영희", "이정수", "이철"]
score = [100, 20, 30, 60, 80]
"""
# 문제 1) 이름을 입력받고 해당 점수를 출력
num1 = 0
name1 = input("이름을 입력하세요: ")
while num1 < 5:
    if name1 == name[num1]:
         print("점수: ", score[num1])
    num1 += 1
"""
"""
# 문제 2) 점수를 입력받고 학생이름 출력
num1 = 0
score1 = int(input("점수를 입력하세요: "))
while num1 < 5:
    if score1 == score[num1]:
        print("해당 점수 학생 이름: ", name[num1])
    num1 += 1
"""
"""
# 문제 3) 이름 2개를 입력받고 해당 학생의 점수 교환
num1 = 0
score3 = 0
name1 = input("이름1을 입력하세요: ")
name2 = input("이름2를 입력하세요: ")
while num1 < 5:
    if name1 == name[num1]:
        score1 = score[num1]
    elif name2 == name[num1]:
        score2 = score[num1]
    num1 += 1
score3 = score2
score2 = score1
score1 = score3
print(name1, "의 점수: ", score1, ", ", name2, "의 점수: ", score2)
"""
"""
# 문제 4) 가장 점수가 높은 학생 이름 출력
max2 = score[0]
num1 = 0
while num1 < 5:
    if max2 < score[num1]:
        max2 = score[num1]
    num1 += 1
num2 = 0
while num2 < 5:
    if max2 == score[num2]:
        print("가장 점수가 높은 학생: ", name[num2])
    num2 += 1
    """
# =========================================================================================
st_info = [["김철수", 100], ["김만수", 20], ["김영희", 30], ["이정수", 40], ["이철", 80]]
"""
# 문제 1) 이름을 입력받고 해당 점수를 출력
name1 = input("이름을 입력하세요: ")
num1 = 0
while num1 < 5:
    if name1 == st_info[num1][0]:
        print("점수: ", st_info[num1][1])
    num1 += 1
"""
"""
# 문제 2) 점수를 입력받고 학생이름 출력
score1 = int(input("점수를 입력하세요: "))
num1 = 0
while num1 < 5:
    if score1 == st_info[num1][1]:
        print("해당 점수 학생 이름: ", st_info[num1][0])
    num1 += 1
"""
"""
# 문제 3) 이름 2개를 입력받고 해당 학생의 점수 교환
name1 = input("이름1을 입력하세요: ")
name2 = input("이름2를 입력하세요: ")
num1 = 0
score3 = 0
while num1 <5:
    if name1 == st_info[num1][0]:
        score1 = st_info[num1][1]
    elif name2 == st_info[num1][0]:
        score2 = st_info[num1][1]
    num1 += 1
score3 = score2
score2 = score1
score1 = score3
print(name1, "의 점수: ", score1, ", ", name2, "의 점수: ", score2)
"""
"""
# 문제 4) 가장 점수가 높은 학생 이름 출력
max1 = st_info[0][1]
num1 = 0
while num1 < 5:
    if max1 < st_info[num1][1]:
        max1 = st_info[num1][1]
    num1 += 1
num2 = 0
while num2 < 5:
    if max1 == st_info[num2][1]:
        print("가장 점수가 높은 학생: ", st_info[num2][0])
    num2 += 1
"""
```

