# function03

```python
def show_nums(num1, num2):
    print(num1)
    print(num2)


show_nums(10, 20)


def show_calc(num1, num2):
    print(num1 + num2)
# 문제 1) 숫자 2개를 넣고 + - * / % ㅡㄹ 출력해보세요
show_calc(10, 3)
def show_lst(lst):
    for i in lst:
        print(i)
lst = [10, 20, 30, 140, -1, 40, 2, 54]
show_lst(lst)

# 문제 1) 리스트안에 짝수만 출력해주는 함수
def show_lst_even(lst):
    for i in lst:
        if i % 2 == 0:
            print(i)
show_lst_even(lst)

# 문제 2) 리스트안의 짝수의 갯수를 출력해주는 함수
def show_lst_even_count(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    print("짝수의 갯수: ", count)
show_lst_even_count(lst)
# 문제 3) 리스트안의 합
def show_lst_total(lst):
    total = 0
    for i in lst:
        total += i
    print("합: ", total)
show_lst_total(lst)
# 문제 4) 가장큰수 함수
def show_lst_max(lst):
    print("가장 큰수: ", max(lst))
show_lst_max(lst)

```

