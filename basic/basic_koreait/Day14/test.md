# test

```python
# 반복문 문제 ==>


# 1. 인덱스 입력받고 값출력
# 2. 값을 입력받고 인뎃 출력
value = int(input("값을 입력하세요"))
for i in range(len(lst)):
    if value == lst[i]:
        print(i)
        break # 찾았으면 더이상 반복할 필요가 없다.
# 3. 가장큰값 출력
# =================================================================================================
# 응용문제 숫자를 넣으면 그 숫자만큼 라인을 그려주는 함수를 만들어보세요 ~
def show_lines(num):
    for i in range(num):
        print("=" * i)
# 응용문제 숫자를 넣으면 짝수인지 홀수인지 출력
def show_lst(lst):
    for i in lst:
        print(i)
show_lst(lst)
# 문제 1) 리스트안에 짝수만 출력해주는함수
def show_lst_even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)
# show_ls_even(lst)
# 문제2) 리스트안의 짝수의 갯수를 출력해주는 함수
# show_lst_even_count(lst)
# 문제3) 리스트안의 합
```

