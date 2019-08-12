# for02

```python
# 문제 2)
lst = []
import random
for i in range(5):
    lst.append(random.randint(0, 100))
    if lst[i] >= 60:
        print("합격 >>", lst[i])
print(lst)

num = 0
while num < 5:
    lst.append(random.randint(0, 100))
    if lst[num] >= 60:
        print("합격 >>", lst[num])
    num += 1
```

