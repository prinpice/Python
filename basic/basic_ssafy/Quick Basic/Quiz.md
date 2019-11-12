# Quiz

**두 개의 정수 n과 m이 주어집니다. 반복문을 사용하지 않고 별(*) 문자를 이용해 가로 의 길이가 n, 세로의 길이가 m인 직사각형 형태를 출력해보세요.**

```python
n = 5
m = 9
print(('*'*n + '\n')*m)
```



**다음 딕셔너리에서 평균 점수를 출력하시오.**

```python
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
sum = 0
for i in student.values():
    sum += i
print(sum/len(student))
```



**다음은 학생들의 혈액형(A, B, AB, O)에 대한 데이터이다. for문을 이용하여 각 혈액형 별 학생수의 합계를 구하시오.**

```python
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
## myway
a, b, o, ab = 0, 0, 0, 0
for i in blood_types:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'O':
        o += 1
    elif i == 'AB':
        ab += 1
print(f'A형 : {a}명, B형 : {b}명, AB형 : {ab}명, O형 : {o}명')

## p's way
result = {}
for bt in blood_types:
    if bt in result:
        result[bt] += 1
    else: 
        result[bt] = 1
print(result)
```



**조건문을 통해 변수 num의 값과 홀수/짝수 여부를 출력하세요**

```
예시 출력)
3
홀수입니다
```

```python
in : 
    # 실습!
	num = int(input("점수를 입력하세요 : "))
	# 아래에 코드를 작성하세요.
	if num % 2 != 0:
    	print("홀수입니다.")
	else:
    	print("짝수입니다.")
out : 
    점수를 입력하세요 : 3
    홀수입니다.
```



**아래 코드의 출력 결과를 예상해보세요**

```python
#코드는 다음과 같습니다. 출력 결과를 예상해보세요. 
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")


out : 3
      5
```



**호날두는 5,000원의 돈을 가지고 있고 카드는 없다고 한다. 이러한 호날두의 상태는 아래와 같이 표현할 수 있을 것이다. 호날두는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하고 있거나 4,000원 이상의 현금을 가지고 있어야 한다고 한다. 호날두는 택시를 탈 수 있는지를 판별할 수 있는 조건식을 작성하고 그 결과를 출력하세요.**

```python
in : 
    money = 5000
	card = False
	if money >= 4000 or card == True:
    	print("택시를 탈 수 있습니다.")
	else:
    	print("택시를 탈 수 없습니다.")
out :
    택시를 탈 수 있습니다.
```



**조건문을 통해 변수 score에 따른 평점을 출력하세요**

| 점수      | 등급 |
| --------- | ---- |
| 90점 이상 | A    |
| 80점 이상 | B    |
| 70점 이상 | C    |
| 60점 이상 | D    |
| 60점 미만 | F    |

```
예시 출력)
B
```

```python
in : 
    # 실습!
	score = int(input("점수를 입력하세요 : "))
	# 아래에 코드를 작성하세요.
	if score >= 90:
    	print("A")
	elif score >= 80:
    	print("B")
	elif score >= 70:
	    print("C")
	elif score >= 60:
	    print("D")
	else:
	    print("F")
out : 
    점수를 입력하세요 : 89
	B
```



**하나에 1000원 하는 연필과 하나에 2000원 하는 펜이 있다. 구입 시 10000원이 넘으면 10%를 할인해 준다고 한다. 구매하고자하는 연필과 펜의 수를 사용자로부터 입력받고 조건문을 활용하여 할인율을 적용하고 최종 구입 금액을 출력하는 프로그램을 작성하시오.**

```python
in : 
    pencil = int(input("구매할 연필 수: "))
    pen = int(input("구매할 펜 수: "))
    sum = pencil * 1000 + pen * 2000
    if sum >= 10000:
        print("합 계 : ", sum * 0.9, "원")
    else:
        print("합 계 : ", sum, "원")
out : 
    구매할 연필 수: 5
    구매할 펜 수: 4
    합 계 :  11700.0 원
```



**다음 코드의 결과값을 예측하세요**

```python
in : 
    # 코드는 여기 있습니다. 결과는 무엇일까요?
    a = "Life is too short, you need python"

    if 'wife' in a:
        print('wife')
    elif 'python' in a and 'you' not in a:
        print('python')
    elif 'shirt' not in a:
        print('shirt')
    elif 'need' in a:
        print('need')
    else:
        print('none')
out : 
    shirt
```



**다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2와 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.**

```python
in : 
    for i in range(1, 101):
    if i % 2 == 0 and i % 11 == 0:
        print(i, "FizzBuzz", end="\t")
    elif i % 2 == 0:
        print(i, "Fizz", end="\t")
    elif i % 11 == 0:
        print(i, "Buzz", end="\t")
    else:
        print(i, end="\t")
out:
    1	2 Fizz	3	4 Fizz	5	6 Fizz	7	8 Fizz	9	10 Fizz	11 Buzz	12 Fizz	13	14 Fizz	15	16 Fizz	17	18 Fizz	19	20 Fizz	21	22 FizzBuzz	23	24 Fizz	25	26 Fizz	27	28 Fizz	29	30 Fizz	31	32 Fizz	33 Buzz	34 Fizz	35	36 Fizz	37	38 Fizz	39	40 Fizz	41	42 Fizz	43	44 FizzBuzz	45	46 Fizz	47	48 Fizz	49	50 Fizz	51	52 Fizz	53	54 Fizz	55 Buzz	56 Fizz	57	58 Fizz	59	60 Fizz	61	62 Fizz	63	64 Fizz	65	66 FizzBuzz	67	68 Fizz	69	70 Fizz	71	72 Fizz	73	74 Fizz	75	76 Fizz	77 Buzz	78 Fizz	79	80 Fizz	81	82 Fizz	83	84 Fizz	85	86 Fizz	87	88 FizzBuzz	89	90 Fizz	91	92 Fizz	93	94 Fizz	95	96 Fizz	97	98 Fizz	99 Buzz	100 Fizz
```



**세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하세요.**

```python
in : 
    # 여기에 코드를 입력하세요1
    A = int(input("정수1을 입력하세요 : "))
    B = int(input("정수2를 입력하세요 : "))
    C = int(input("정수3을 입력하세요 : "))
    max = A
    min = A
    if max < B:
        max = B
    if max < C:
        max = C
    if min > B:
        min = B
    if min > C:
        min = C

    if A != max and A != min:
        print("A=", A)
    elif B != max and B != min:
        print("A=", A)
    elif C != max and C != min:
        print("A=", A)


    #여기에 코드를 입력하세요2
	a, b, c = map(int, input().split())
out : 
    정수1을 입력하세요 : 5
    정수2를 입력하세요 : 3
    정수3을 입력하세요 : 7
    A= 5
```



**사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하세요. 각 통화별 환율은 다음과 같습니다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정합니다.**

```python
in : 
    str = input("환전할 금액을 입력하세요: ")
    str_list = str.split(" ")
    if "달러" in str_list:
        print(str + "은", 1126.20 * int(str_list[0]), "원 입니다.")
    elif "엔" in str_list:
        print(str + "은", 1046.5 * int(str_list[0]), "원 입니다.")
    elif "유로" in str:
        print(str + "은", 1277.62 * int(str_list[0]), "원 입니다.")
    elif "위안" in str:
        print(str + "은", 163.53 * int(str_list[0]), "원 입니다.")
out : 
    환전할 금액을 입력하세요: 1000 달러
	1000 달러은 1126200.0 원 입니다.
```



**표준 입력으로 나이(만 나이)가 입력됩니다(입력 값은 7 이상 입력됨). 교통카드 시스템에서 시내버스 요금은 다음과 같으며 각 나이에 맞게 요금을 차감한 뒤 잔액이 출력되게 만드세요. 현재 교통카드에는 9,000원이 들어있습니다.**

```python
in :
    money = 9000
    adult = 1200
    child = 700
    age = int(input("나이를 입력하세요 : "))
    if age < 20:
        print("잔액은", money - chlid, "원 입니다.")
    else : 
        print("잔액은", money - adult, "원 입니다.")
out : 
    나이를 입력하세요 : 21
	잔액은 7800 원 입니다.
```



**영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다. 영어 이름을 입력받아 가운데 이름은 축약해서 나타내는 코드를 작성해보세요
예시 입력) Alice Betty Catherine Davis
예시 출력) Alice B. C. Davis**

```python
in : 
    str_name = input()
    lst_name = str_name.split(" ")
    result = lst_name[0] + " "
    for i in range(1, len(lst_name)-1):
        result += lst_name[i][0:1] + ". "
    result += lst_name[-1]
    print(result)
out : 
    Alice Betty Catherine Davis
	Alice B. C. Davis
```



**1부터 1000까지의 자연수 중 5의 배수에 해당되는 자연수들의 총합을 구하세요.**

```python
in : 
    sum = 0
    for i in range(1, 1001):
        if i % 5 == 0:
            sum += i
    print(sum)
out : 
    100500
```



**반복문과 조건문만 활용하여 1~30까지 숫자 중에 홀수만 담긴 리스트를 만드세요**

```python
예시 출력)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
```

```python
in : 
    lst_odd = []
    for i in range(1, 31):
        if i % 2 != 0:
            lst_odd.append(i)
    print(lst_odd)
out : 
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
```



**1부터 100까지 자연수를 모두 더하고 그 결과를 출력하세요**

```python
in : 
    sum = 0
    i = 1
    while i <= 100:
        sum += i
        i += 1
    print(sum)
out : 
    5050
```



**1부터 1000까지 자연수 중 3의 배수의 합을 구하세요**

```python
in : 
    sum = 0
    i = 1
    while i <= 1000:
        if i % 3 == 0:
            sum += i
        i += 1
    print(sum)
out : 
    166833
```



**다음은 A학급 학생들의 수학 점수 리스트입니다. 다음 리스트에서 50점 이상의 점수들의 총합을 구하세요. for문과 while문을 각각 활용해서 2개의 답을 작성해주세요.**

```python
in : 
    scores = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
    sum_for = 0
    sum_while = 0

    for i in scores:
        if i >= 50:
            sum_for += i
    print(sum_for)

    count = 0
    while count < len(scores):
        if scores[count] >=50:
            sum_while += scores[count]
        count += 1
    print(sum_while)
out : 
    481
```

```python
in : 
    scores=[20,55,67,82,45,33,90,87,100,25]

    result = 0 
    while scores:
        picker = scores.pop()
        if picker >=50:
            result+=picker
    print(result)
out : 
    
```



**while문을 활용하여 아래와 같은 역삼각형의 asterisk를 출력하는 코드를 작성하세요**

```python
# *******
#  *****
#   ***
#    *
```

```python
in : 
    count = 4
    while count > 0:
        print(" "*(4-count), end="")
        print("*"*(2*count-1))
        count -= 1
out : 
    *******
     *****
      ***
       *
```



**0과 73사이의 숫자 중 3으로 끝나는 숫자만 출력되게 하는 코드를 작성하세요**

```python
in : 
    for i in range(0, 74):
        if i % 10 == 3:
            print(i)
out : 
    3
    13
    23
    33
    43
    53
    63
    73
```



**한잔에 300원인 커피 10개를 팔 수 있도록 하는 자판기의 코드를 while문과 if문을 활용하여 코드로 작성하세요**

```python
in : 
    count = 0
    while count < 10:
        num = int(input("구매하고자 하는 커피의 수를 입력하세요: "))
        if (10-count) < num:
            print("개수를 초과했습니다.")
            return
        print(f"가격은 {num * 300}원 입니다.")
        count += num
        print(f"남은 커피의 수 : {10-count}개")
    print("판매완료했습니다.")
out : 
    구매하고자 하는 커피의 수를 입력하세요: 5
    가격은 1500원 입니다.
    남은 커피의 수 : 5개
    구매하고자 하는 커피의 수를 입력하세요: 6
    개수를 초과했습니다.
    구매하고자 하는 커피의 수를 입력하세요: 3
    가격은 900원 입니다.
    남은 커피의 수 : 2개
    구매하고자 하는 커피의 수를 입력하세요: 3
    개수를 초과했습니다.
    구매하고자 하는 커피의 수를 입력하세요: 2
    가격은 600원 입니다.
    남은 커피의 수 : 0개
    판매완료했습니다.
```



**n이 입력으로 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하세요.**

```python
in : 
    n = int(input())
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
out :
    5
	15
```



**for와 range 함수를 이용하여 구구단 결과를 출력하세요.**

```python
in : 
    for i in range(1, 10):
        for j in range(1, 10):
            print( i, "*", j, "=", i * j)
        print("\n")
out : 
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    1 * 4 = 4
    1 * 5 = 5
    1 * 6 = 6
    1 * 7 = 7
    1 * 8 = 8
    1 * 9 = 9


    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    2 * 4 = 8
    2 * 5 = 10
    2 * 6 = 12
    2 * 7 = 14
    2 * 8 = 16
    2 * 9 = 18


    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    3 * 4 = 12
    3 * 5 = 15
    3 * 6 = 18
    3 * 7 = 21
    3 * 8 = 24
    3 * 9 = 27


    4 * 1 = 4
    4 * 2 = 8
    4 * 3 = 12
    4 * 4 = 16
    4 * 5 = 20
    4 * 6 = 24
    4 * 7 = 28
    4 * 8 = 32
    4 * 9 = 36


    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45


    6 * 1 = 6
    6 * 2 = 12
    6 * 3 = 18
    6 * 4 = 24
    6 * 5 = 30
    6 * 6 = 36
    6 * 7 = 42
    6 * 8 = 48
    6 * 9 = 54


    7 * 1 = 7
    7 * 2 = 14
    7 * 3 = 21
    7 * 4 = 28
    7 * 5 = 35
    7 * 6 = 42
    7 * 7 = 49
    7 * 8 = 56
    7 * 9 = 63


    8 * 1 = 8
    8 * 2 = 16
    8 * 3 = 24
    8 * 4 = 32
    8 * 5 = 40
    8 * 6 = 48
    8 * 7 = 56
    8 * 8 = 64
    8 * 9 = 72


    9 * 1 = 9
    9 * 2 = 18
    9 * 3 = 27
    9 * 4 = 36
    9 * 5 = 45
    9 * 6 = 54
    9 * 7 = 63
    9 * 8 = 72
    9 * 9 = 81
```



**표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요. 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.**

```python
in : 
    num = int(input())
    for i in range(1, num+1):
        print(" " * (num-i), end="")
        print("*" * (i*2 - 1))
out : 
    5
        *
       ***
      *****
     *******
    *********
```



**colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape'] 다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하시오.**

```python
in : 
    colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
    fruit = [color for (a, color) in enumerate(colors) if a not in (0, 4, 5)]
    print(fruit)
out : 
    ['Banana', 'Coconut', 'Deli']
```



**4가지 반복문을 활용해보고 출력되는 결과를 확인해보세요.**

```python
classroom = {"teacher": "Kim", "student1": "Hong", "student2": "Kang"}
```

```python
in :
    classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
    for key in classroom:
        print(key)
out :
    teacher
    student1
    student2
```

```python
in :    
    classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
    for key in classroom.keys():
        print(key)
out :   
    teacher
    student1
    student2
```

```python
in :    
    classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
    for val in classroom.values():
        print(val)
out : 
    Kim
    Hong
    Kang
```

```python
in :    
    classroom = {"teacher":"Kim","student1":"Hong","student2":"Kang"}
    for key, val in classroom.items():
        print(key, val)
out : 
    teacher Kim
    student1 Hong
    student2 Kang
```



**조건문과 반복문, break를 통해서 아래의 코드와 동일한 코드를 작성하세요. (3이 있을 경우 True를 print하고, 아닐 경우 False를 print 합니다.)**

```python
numbers = [1, 5, 10]
print(3 in numbers)
```

```python
예시 출력)
False
```

```python
in : 
    numbers = [1, 5, 10]
	while True:
    	if 3 in numbers:
        	print(True)
	    else:
    	    print(False)
    	break
out : 
    False
```



**0과 73사이의 숫자 중 3으로 끝나는 숫자만 출력되게 하는 코드를 작성하세요**

```python
in : 
    i = 0
    while True:
        if i % 10 != 3:
            i += 1
            continue
        if i > 73:
            break
        print(i, end=' ')
        i += 1
out : 
    3 13 23 33 43 53 63 73 
```



**1부터 100까지 자연수를 각각 제곱해 더한 값인 '제곱의 합'과 1부터 100을 먼저 더한 다음에 그 결과를 제곱한 '합의 제곱'의 차이를 구하는 코드를 작성하세요**

```python
in : 
    sum_a = 0
    sum_b = 0
    for i in range(101):
        sum_a += i**2
        sum_b +=i
    print(sum_a - (sum_b**2))
out : 
    -25164150
```



**문자열 요소로만 이루어진 다음과 같은 리스트를 넣었을 때 (samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']my), 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 코드를 작성하세요.**

```python
in :
    samples = ['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']
    count = 0
    for i in samples:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    print(count)
out : 
    3
```



**items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 다음 리스트에서 중복된 요소를 제거한 리스트를 출력하세요.**

```python
in :
    items = [10,20,40,20,10,30,50,60,40,80,50,40,20,30,10] 
    item = []
    for i in items:
        if i not in item:
            item.append(i)
    print(item)
out : 
    [10, 20, 40, 30, 50, 60, 80]
```



**colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']다음 리스트에서 0번째 4번째 5번째 요소를 지운 새로운 리스트를 생성하세요. (위의 예제에서 사용했던 enumerate 메소드가 아닌 다른 방법들을 사용해서 자유롭게 풀어보세요)**

```python
in :
    colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
    fruit = []
    for i in range(1, 4):
        fruit.append(colors[i])
    print(fruit)
out : 
    ['Banana', 'Coconut', 'Deli']
```



**아래의 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하세요.**

```python
나이:30,키:180
```

```python
in :
    str = "나이:30,키:180"
    age_temp, height_temp = str.split(",")
    age_lst = age_temp.split(":")
    height_lst = height_temp.split(":")
    if int(age_lst[1]) < 30 and str(height_lst[1]) >= 175:
        print("YES")
    else:
        print("NO")
out : 
    NO
```



**1월부터 12월까지 다음과 같은 형태로 달력이 출력되도록 코드를 작성하세요.**

```python
1 월
일 월 화 수 목 금 토
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
2 월
일 월 화 수 목 금 토
1 2 3 4 5 6 7
8 9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
```

```python
in :
    month = 1

    while month <= 12:
        print(f'{month}월')
        print("일 월 화 수 목 금 토")
        if month not in (2, 4, 6, 9, 11):
            for i in range(1, 32):
                    print(i, end=" ")
                    if i % 7 == 0:
                        print()
            print()
        else:
            if month == 2:
                for i in range(1, 29):
                    print(i, end=" ")
                    if i % 7 == 0:
                        print()
            else:
                for i in range(1, 31):
                    print(i, end=" ")
                    if i % 7 == 0:
                        print()
                print()
        print()
        month += 1
out : 
    1월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    2월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 

    3월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    4월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 

    5월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    6월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 

    7월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    8월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    9월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 

    10월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 

    11월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 

    12월
    일 월 화 수 목 금 토
    1 2 3 4 5 6 7 
    8 9 10 11 12 13 14 
    15 16 17 18 19 20 21 
    22 23 24 25 26 27 28 
    29 30 31 
```

