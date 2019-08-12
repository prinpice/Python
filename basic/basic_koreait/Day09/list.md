# list

```python
# 리스트

list1 = [10, 20, 30, 40] # 인덱스는 0부터 시작한다. size = 4, index 0, 1, 2, 3
print(list1) # [10, 20, 30, 40 , 50 , 60 70, 80]

num = 10
"""
index = None
index = 0
list1[0] # 10 # 변수 하나
list[index]
index += 1
list1[1]
list1[index] # list1[1]
index += 1
list1[2]
list1[3]
"""
"""
# 1. 인덱스 1개를 입력받고 값을 출력
index = int(input("인덱스를 입력하세요 >>> "))
print(list1[index])
"""
"""
# 2. 전체 합과 평균 출력
total = 0
index = 0
while index <len(list1):
    total += list1[index]
    index += 1
print("전체 합: ", total)
ave = total / len(list1)
print("평균: ", ave)
"""

word_list = ["cpp", "python", "java", "jsp", "c#", "c", "android"]
"""
# 응용문제 1) 단어가 하나씩 프린트 되고 입력해서 단어를 맞추면 count 증가
end = 0
count1 = 0
index = 0
while end == 0 and index < len(word_list):
    print(word_list[index])
    word_input = input("단어를 입력하세요 >>> ")
    if word_input == word_list[index]:
        print("맞췄습니다.")
        count1 += 1
    else:
        print("틀렸습니다.")
    index += 1
print("맞춘 개수:", count1)
"""
# 응용문제 2) 랜덤으로 인덱스를 0 ~ max 까지 뽑는다. 0번이랑 교환 100번 반복 ==>로또
"""
import random
end = 0
max1 = len(word_list)
while end <100:
    index = random.randint(0, max1-1)
    temp = word_list[index]
    word_list[index] = word_list[0]
    word_list[0] = temp
    print(word_list[0])
    end += 1
"""

# 심화문제 3) 단어하나를 * 로 표기 (20일까지)
import random
end = 0
max1 = len(word_list)
while end <100:
    index = random.randint(0, max1-1)
    temp = word_list[index]
    word_list[index] = word_list[0]
    word_list[0] = temp
    max2 = len(word_list[0])
    num1 = 0
    num = random.randint(0, max2-1)
    word1 = word_list[0]
    while num1 <max2:
        if num1 != num:
            print(word1[num1], end="")
        else:
            print("*", end="")
        num1 += 1
    print("\n")
    end += 1
```

