# ex

```python
# 단어에 * 2개 표기
import random
lst= ["entrance", "communication", "volunteer", "alphabet", "outdoor"]
num4 = 0
while num4 < 10:
    num = random.randint(0, len(lst)-1)
    word = lst[num]
    print(word)
    num1 = random.randint(0, len(word)-1)
    num2 = random.randint(0, len(word)-1)
    while num2 == num1:
        num2 =random.randint(0, len(word)-1)
    num3 = 0
    while num3 < len(word):
        if num1 == num3 or num2 == num3:
            print("*", end="")
        else:
            print(word[num3], end="")
        num3 += 1
    print("")
    num4 += 1
```

