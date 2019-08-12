# dictionary

```python
# 딕셔너리 (dictionary)
"""
1. 사전에서 "단어를 기준으로 해설"을 찾듯이
    "키를 기준으로 값"을 찾는 기능을 제공한다. ==> 키 ==> 인덱스 ==> 내가 원하는데로 설정할 수 있다.
2. 구조 { key1 : value1, key2 : value2, key3 : value3 ....}
3. key 는 변하지 않는다.
4. 순서가 없다.
"""
lst = [10, 20] # 값을 저장하면 인덱스는 0부터 순차적으로 자동으로 저장된다.
print(lst[0]) # 10

di = {"키" : 10, "키2" : 20, 3 : 30} # 인덱스(키)를 내맘대로 정할 수 있다.

print(di["키"]) # 10
print(di[3])   # 30

st_info = {"이름": "김철수", "나이": 20, "전화": "010-111-222", "주소": "신촌"}
print(st_info["이름"]) # 김철수

st_info["생일"] = "3/20" # 추가하는 법
print(st_info)

del(st_info["생일"])
print(st_info)

st_info = [
    {"이름": "kim", "나이": 21, "python": 80, "java": 70, "c++": 60},
    {"이름": "lee", "나이": 31, "python": 40, "java": 44, "c++": 2},
    {"이름": "park", "나이": 27, "python": 10, "java": 100, "c++": 6},
    {"이름": "kang", "나이": 11, "python": 6, "java": 74, "c++": 40},
]
# 학생별 종합 평균
for i in range(4):
    sum1 = st_info[i]["python"]+ st_info[i]["java"] +st_info[i]["c++"]
    ave1 = sum1/3
    print(st_info[i]["이름"], ":", ave1, "점")

# 과목별 종합 평균
sum2 = 0
sum3 = 0
sum4 = 0
for j in range(4):
    sum2 += st_info[j]["python"]
    sum3 += st_info[j]["java"]
    sum4 += st_info[j]["c++"]
ave2 = sum2/3
ave3 = sum3/3
ave4 = sum4/3
print("python: ", ave2, "점\njava: ", ave3, "점\nc++: ", ave4, "점")
# 과목별 점수가 가장 낮은 학생 이름
num1 = 0
num2 = 0
num3 = 0
for i in range(4):
    if st_info[num1]["python"] > st_info[i]["python"]:
        num1 = i
    if st_info[num2]["java"] > st_info[i]["java"]:
        num2 = i
    if st_info[num3]["c++"] > st_info[i]["c++"]:
        num3 = i
print("python: ", st_info[num1]["이름"], ", java: ", st_info[num2]["이름"], ", c++: ", st_info[num3]["이름"])
# 전과목중 가장 점수가 낮은 학생 이름
num1 = 0
num2 = 0
num3 = 0
for i in range(4):
    if st_info[num1]["python"] > st_info[i]["python"]:
        num1 = i
    if st_info[num2]["java"] > st_info[i]["java"]:
        num2 = i
    if st_info[num3]["c++"] > st_info[i]["c++"]:
        num3 = i
if st_info[num1]["python"] < st_info[num2]["java"]:
    if st_info[num1]["python"] < st_info[num3]["c++"]:
        print("이름: ", st_info[num1]["이름"])
    else:
        print("이름: ", st_info[num3]["이름"])
else:
    if st_info[num2]["java"] < st_info[num3]["c++"]:
        print("이름: ", st_info[num2]["이름"])
    else:
        print("이름: ", st_info[num3]["이름"])
# 나이가 20 세 이하인 학생 정보 삭제
for i in range(4):
    if st_info[i]["나이"] <= 20:
        del(st_info[i])
print(st_info)
# 총점 항목 추가 "총점 : ???"
```

