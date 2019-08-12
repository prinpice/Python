# test

```python
# 반복문 문제 1) 0 ~ 10 까지 출력, 0 ~ 10까지 합출력
total = 0
for i in range(0, 11):
    print(i)
    total += i
print("합: ", total)
lst1 = [10, 20, 1, -20, 2320, 100]
# 문제 1) 전체합 출력 # 문제 2) 값 입력받고 인덱스 출력
# 문제 3) 가장 큰 값 찾기 # 문제 4) 인덱스 2개 입력받고 서로 교환
# 문제 1 ) 아래 기능을 추가해 보세요~
"""
lst_names = ["김철수", "박만수", "이영희"]
lst_scores = [100, 80, 55]
lst_names.append("???")
print(lst_names)
lst_names.remove(lst_names[3])
print(lst_names)
end = 0
while end == 0:
    print("***** 학생관리 프로그램 *****")
    print("1. 추가\n2. 삭제\n3. 번호검색\n4. 이름검색\n5. 전체조회\n6. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        name = input("이름을 입력하세요 >> ")
        score = int(input("점수를 입력하세요 >>"))
        lst_names.append(name)
        lst_scores.append(score)
    if sel == 2:
        name = input("삭제할 이름을 입력하세요 >> ")
        for i in range(0, len(lst_names)):
            if name == lst_names[i]:
                lst_names.remove(lst_names[i])
                lst_scores.remove(lst_scores[i])
                break # 보조제어문 ==> 반복문을 즉시 빠져나간다.
    if sel == 3:
        score = int(input("번호르 입력하세요 >> "))
        for i in range(0, len(lst_scores)):
            if score == lst_scores[i]:
                print("이름: ", lst_names[i])
                print("점수: ", lst_scores[i])
    if sel == 4:
        name = input("이름을 입력하세요 >> ")
        for i in range(0, len(lst_names)):
            if name == lst_names[i]:
                print("이름: ", lst_names[i])
                print("점수: ", lst_scores[i])
    if sel == 5:
        print(lst_names)
        print(lst_scores)
    if sel == 6:
        end = 1
"""
# 문제 2) 위 기능을 아래 data 로 해결해보세요
lst_st_info = [["김철수", 100], ["박만수", 80], ["이영희", 55]]
print(lst_st_info)

end = 0
while end == 0:
    print("***** 학생관리 프로그램 *****")
    print("1. 추가\n2. 삭제\n3. 번호검색\n4. 이름검색\n5. 전체조회\n6. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        name = input("이름을 입력하세요 >> ")
        score = int(input("점수를 입력하세요 >>"))
        lst_st_info.append([name, score])
    if sel == 2:
        name = input("삭제할 이름을 입력하세요 ")
        for i in range(0, len(lst_st_info)):
            if name == lst_st_info[i][0]:
                lst_st_info.remove(lst_st_info[i])
                break # 보조제어문 ==> 반복문을 즉시 빠져나간다.
    if sel == 3:
        score = int(input("번호르 입력하세요 >> "))
        for i in range(0, len(lst_st_info)):
            if score == lst_st_info[i][1]:
                print("이름: ", lst_st_info[i][0])
                print("점수: ", lst_st_info[i][1])
    if sel == 4:
        name = input("이름을 입력하세요 >> ")
        for i in range(0, len(lst_st_info)):
            if name == lst_st_info[i][0]:
                print("이름: ", lst_st_info[i][0])
                print("점수: ", lst_st_info[i][1])
    if sel == 5:
        print(lst_st_info)
    if sel == 6:
        end = 1

```

