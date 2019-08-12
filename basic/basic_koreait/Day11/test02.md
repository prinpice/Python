# test02

```python
"""
names = ["aaa", "bbb", "ccc", "ddd"]
scores = [100, 30, 70, 2]
end = 0
while end == 0:
    print("학생 관리 프로그램")
    print("1. 등록")
    print("2. 삭제") # 이름으로 삭제
    print("3. 조회") # 1. 전체, 2. 이름 3. 성적순으로 출력(심화)
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        name1 = input("이름을 입력하세요 >>> ")
        names.append(name1)
        score1 = int(input("점수를 입력하세요 >>> "))
        scores.append(score1)
    elif sel == 2:
        name2 = input("이름을 입력하세요 >>> ")
        num1 = 0
        while num1 < len(names):
            if name2 == names[num1]:
                names.remove(names[num1])
                scores.remove(scores[num1])
            num1 += 1
    elif sel == 3:
        print("1. 전체")
        print("2. 이름")
        print("3. 성적순")
        sel1 = int(input("번호를 입력하세요 >>> "))
        if sel1 == 1:
            print("이름: ", names)
            print("점수: ", scores)
        elif sel1 == 2:
            name3 = input("이름을 입력하세요 >>> ")
            num2 = 0
            while num2 < len(names):
                if name3 == names[num2]:
                    print("이름: ", names[num2])
                    print("점수: ", scores[num2])
                num2 += 1
        elif sel1 == 3:
            num4 = 0
            while num4 < 6:
                num3 = 0
                while num3 < len(scores) - 1:
                    score_temp = scores[num3]
                    name_temp = names[num3]
                    if score_temp < scores[num3 + 1]:
                        scores[num3] = scores[num3 + 1]
                        scores[num3 + 1] = score_temp
                        names[num3] = names[num3 + 1]
                        names[num3 + 1] = name_temp
                    num3 += 1
                num4 += 1
            print(names)
            print(scores)
    elif sel == 4:
            end = 1
"""
# ===============================================================================================
"""
end = 0
lst1 = [200, -100, 20, 30 , 50, 80]
while end == 0:
    print("학생 관리 프로그램")
    print("1. 등록")
    print("2. 삭제") # 번호
    print("3. 조회") # 전체
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        num1 = int(input("번호를 입력하세요 >>> "))
        lst1.append(num1)
    elif sel == 2:
        num2 = int(input("번호를 입력하세요 >>> "))
        num3 = 0
        while num3 < len(lst1):
            if num2 == lst1[num3]:
                lst1.remove(lst1[num3])
            num3 += 1
    elif sel == 3:
        print("전체 번호:", lst1)
    elif sel == 4:
        end = 1
"""
# === 심화 =============================================================================================
st_info = [["aaa", 10], ["bbb", 20], ["ccc", 400], ["rrr", 80]]
end = 0
while end == 0:
    print("학생 관리 프로그램")
    print("1. 등록")
    print("2. 삭제")  # 이름으로 삭제
    print("3. 조회")  # 1. 전체, 2. 이름 3. 성적순으로 출력(심화)
    print("4. 종료")
    sel = int(input("번호를 입력하세요 >>> "))
    if sel == 1:
        name1 = input("이름을 입력하세요 >>> ")
        score1 = int(input("점수를 입력하세요 >>> "))
        st_info.append([name1, score1])
    elif sel == 2:
        name2 = input("이름을 입력하세요 >>> ")
        num1 = 0
        while num1 < len(st_info):
            if name2 == st_info[num1][0]:
                st_info.remove(st_info[num1])
        num1 += 1
    elif sel == 3:
        print("1. 전체")
        print("2. 이름")
        print("3. 성적순")
        sel1 = int(input("번호를 입력하세요 >>> "))
        if sel1 == 1:
            print(st_info)
        elif sel1 == 2:
            name3 = input("이름을 입력하세요 >>> ")
            num2 = 0
            while num2 < len(st_info):
                if name3 == st_info[num2][0]:
                    print(st_info[num2])
                num2 += 1
        elif sel1 == 3:
            num4 = 0
            while num4 < 6:
                num3 = 0
                while num3 < len(st_info) - 1:
                    st_info_temp_score = st_info[num3][1]
                    st_ino_temp_name = st_info[num3][0]
                    if st_info_temp_score < st_info[num3 + 1][1]:
                        st_info[num3][1] = st_info[num3 + 1][1]
                        st_info[num3 + 1][1] = st_info_temp_score
                        st_info[num3][0] = st_info[num3 + 1][0]
                        st_info[num3 + 1][0] = st_ino_temp_name
                    num3 += 1
                num4 += 1
        print(st_info)
    elif sel == 4:
        end = 1



```

