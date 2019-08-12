# function02

```python
"""
i = 10

def test():
    i = 20

print(i)
test()
print()
i = test()
print(i)
"""

num = 200
def test1(num):
    num += 100
    return num # 잠깐 살아있는다.이때 데이터를 넘겨받아야한다.
print(num) #200
test1(num)
print(num) # 200
```

