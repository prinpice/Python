# test01

```python
monster_name = ["거대박쥐", "야생늑대", "공룡"]
monster_hp = [100, 50, 200]
monster_pow = [10, 20, 14]
player_hp = [80, 100, 120]
player_pow = [10, 11, 12]
player_skill = [20, 30, 40]
def show_mon_info():
    print("----- TEXT_GAME -----")
    for i in range(len(monster_name)):
        print("이름 >>", monster_name[i], end=" ㅣ")
        print("체력 >>", monster_hp[i], end=" ㅣ")
        print("파워 >>", monster_pow[i], end=" ㅣ")
        print()
while True:
    show_mon_info()
    input()
# ==================================================================
lst = [10, 6, -7, 200, 5, -9]
# 함수
# 문제 1) 리스트안에 짝수만 출력해주는 함수
print(lst)
def show_even_info(lst):
    for i in lst:
        print(i)
        print(lst[i])
        if lst[i] % 2 == 0:
            print(lst[i])
show_even_info()
# 문제 2) 리스트안의 짝수의 갯수를 출력해주는 함수
# 문제 3) 리스트 안의 합을 출력해주는 함수
# ==================================================================
# 리스트
# 문제 1) 리스트 안의 합을 출력
# 문제 2) 리스트 안의 짝수만 출력
# 문제 3) 값을 입력받고 인덱스 출력
# 문제 4) 가장 큰 값 출력
```

