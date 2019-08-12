# test02

```python
# 369 게임 ==> 1~ 50까지 출력을 하는데 359 ==> 1개면 "짝"  369 ==> 2개면 "짝짝"

# 1, 2, 짝, 4, 5, 짝, 7, 8, 짝

num = 1
while num < 50:
    while num < 11:
        num1 = str(num)
        if num1 != "3" and num1 != "6" and num1 != "9":
            print(num, " , ", end="")
        else:
            print("짝 , ", end="")
        num += 1
    print("\n")
    while num <50:
        num1 = str(num)
        if num1[1] == "3" or num1[1] == "6" or num1[1] == "9":
            if num1[0] == "3" or num1[0] == "6" or num1[0] == "9":
             print("짝짝 , ", end="")
            else:
                print("짝 , ", end="")
        else:
            if num1[0] == "3" or num1[0] == "6" or num1[0] == "9":
             print("짝 , ", end="")
            else:
                print(num, " , ", end="")
        if num % 10 == 0:
            print("\n")
        num += 1
    print(num)

```

