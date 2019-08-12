# list02

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
index = 0
print(list1[0])
print(list1[index])

# while index <= len(list1): pass

while index < 8:
    print(list1[index]) # index 가 0 ~ 7 까지 차례로 변한다.
    index += 1

list1 = ["철수", "민수", "영희", "민정", "만수"]

# 문제 1) 인덱스를 입력받고 학생 이름 출력 ==> 예 0 ==> 철수 , 3 ==> 민정
index = int(input("인덱스를 입력하세요(0~4) >>> "))
print(list1[index])

# 문제 2) 이름을 입력받고 인덱스 출력 ==> 예) 만수 ==> 3 , 영희 ==> 2
name = input("이름을 입력하세요 >>> ")
index = 0
while name != list1[index]:
    index += 1
print(index)
"""
while index <len(list1): # 5
    if name == list1[index]:
        print("인덱스 :", index)
        index += 1  # 탈출조건!!!
"""
# if 문제 ==> 숫자 하나를 입력받고 짝수 홀수 양수 음수 0 출력
# while 문제 ==> 0 ~ 10 까지 짝수만 다 더한 값 출력
# list 문제 ==> 위에 2개

# list 추가 문제 1) # 1. 인덱스를 입력받고 값 출력, 2. 값을 입력받고 인덱스 출력
# 3. 인덱스 2개를 입력받고 값교환
# 4. 짝수의 갯수 출력 , 양수의 갯수 출력
list1 = [100, -9, 10, 1, 8, 203, 4]
# 1
index = 7
while index < 0 or index > 6:
    index = int(input("인덱스를 입력하세요(0~6) >>> "))
    if index <0 or index > 6:
        print("잘못 입력하셨습니다.")
print(list1[index])

# 2
```

