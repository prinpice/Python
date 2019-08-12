# test01

```python
# 1. 저장 (자료구조) ==> 1) 변수 , 2) 리스트(배열)
# 2. 수정 (알고리즘) ==> 1) 연산자 2) 조건문 3) 반복문

# 연산자 문제 ==> 숫자 2개를 입력받고 산술연산을 출력 + - * / // %
# 조건문 문제 ==> 숫자 하나를 입력받고 짝수 홀수 양수 음수 0 출력
# 반복문 문제 ==> 0~10 까지 짝수만 다 더한 값 출력

list1 = [100, -9, 10, 1, 8, 203, 4]
# 1. 인덱스를 입력받고 값 출력
"""
index = int(input("인덱스를 입력하세요 >>> "))
print(list1[index])
"""
"""
index1 = int(input("인덱스를 입력하세요 >>> "))
print(list1[index1])
"""
# 2. 값을 입력받고 인덱스 출력
"""
index = 0
num = input("값을 입력하세요 >>> ")
while index < len(list1):
    if num == list1[index]:
        print(num)
    index += 1
"""
"""
value1 = int(input("값을 입력하세요 >>> "))
num = 0
while num < len(list1):
    if value1 == list1[num]:
        print(num)
    num += 1
"""
# 3. 인덱스 2개를 입력받고 값 교환
"""
index1 = int(input("인덱스1"))
index2 = int(input("인덱스2"))
temp = list1[index1]
list1[index1] = list1[index2]
list1[index2] = temp
print(list1)
"""
# 4. 짝수의 갯수 출력 , 양수의 갯수 출력
"""
count1 = 0
count2 = 0
while num <len(list1):
    if list1[num] % 2 == 0:
        count1 += 1
    if list[num] > 0:
        count2 += 1
    num += 1
print("짝수:", count1)
print("양수:", count2)
"""
# 5. 전체 함 출력 , 평균 출력

total = 0
num = 0
while num < len(list1):
    total += int(list1[num])
    num += 1
print("전체 합: ", total)
ave = total / len(list1)
print("평균 :", ave)
# 6. 가장큰수 찾기 ==> 203
num = 0
max1 = list1[0]
while num < len(list1):
    if max1 < list1[num]:
        max1 = list1[num]
    num += 1
print(max1)



```

