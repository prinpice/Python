# numpy02

```python
import numpy as np

arr = np.arange(10)
print(arr)
print(arr[8]) # 8
print(arr[3:5]) # [3 4]
arr[1:5] = 100
print(arr) # [  0 100 100 100 100   5   6   7   8   9]

arr2d = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(arr2d[2, :]) # [ 9 10 11 12] ==> 세로 0, 1, 2 가로 : 전부
print(arr2d[1:3, :]) # [[ 5  6  7  8]
                     #  [ 9 10 11 12]]
print(arr2d[:, 1]) # [ 2  6 10]

# 문제 1) 2367 자르기
print(arr2d[0:2, 1:3]) # [[2 3]
                       #  [6 7]]

```

