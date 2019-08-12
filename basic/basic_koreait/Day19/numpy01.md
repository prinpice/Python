# numpy01

```python
import numpy as np  # as np : numpy 를 줄여서 앞으로 np 로 사용하겠다

# 자료구조 // 1. 변수, 2. 리스트, 3. 딕셔너리, 4. 넘파이


data1 = [6, 7, 8, 9, 10]
arr1 = np.array(data1) # 배열 == 리스트


print(arr1) # [6, 7, 8, 9, 10]
print(arr1.shape) # (5,)

data2 = [[1, 2, 3], [4, 5, 6]]
print(data2) #[[1, 2, 3], [4, 5, 6]]
arr2 = np.array(data2)
print(arr2) # [[1, 2, 3]
            #  [4, 5, 6]]
# 2차원 이상 바둑판배열에서 리스트보다 편함


print(np.arange(15)) # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(arr1.dtype) # int32 ==> +- 20억
arr3 = np.array([1, 2, 3, 4, 5], dtype = np.int64)
float_arr1 = arr3.astype(np.float64)
print(float_arr1.dtype) # float64

arr4 = np.array([[1, 2, 3], [4, 5, 6]])
arr5 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr4 + arr5) # [[ 2  4  6]
                   #  [ 8 10 12]]
print(arr4 - arr5) # [[0 0 0]
                   #  [0 0 0]]
print(arr4 * arr5) # [[ 1  4  9]
                   #  [16 25 36]]
print(arr4 / arr5) # [[1. 1. 1.]
                   #  [1. 1. 1.]]
```

