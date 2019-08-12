# while02

```python
"""
1. while ===> 키워드
2. 조건 : --> 조건종료 ==> 조건이 True 이면 실행문 실행
3. 들여쓰기 ==> 들여쓰기한 영역이 실행문 영역이다. ==> 실행문 종료 후 조건으로 다시 올라간다.
4. 탈출조건 ==> 반드시 필요하다.
        1) 초기식 ==> num = 0
        2) 조건식 ==> num < 10:
        3) 증감식 ==> num +=1  ==> num = num + 1
"""

"""
num = 0

while num <10:
    print("실행문")
    # num += 1  # num = num + 1 의 축약형
    print("num", num)
    num += 1
print("종료")
"""
# 문제 1) 10 ~ 20 까지 출력을 해보세요(반복문 사용)
num = 10
while num <=20:
    print(num)
    num +=1
print("종료")

# 문제 2) 0~5 까지 출력 and 10~15 까지 출력해보세요 (반복문, 조건문)
num = 0
while num <=15:
    if num <= 5 or num >= 10:
        print(num)
    num +=1
print("종료")
```

