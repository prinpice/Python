# numpy01

```python
import numpy as np

data = np.loadtxt("movielens-1m/ratings.dat", delimiter="::", dtype = np.int64)

print(data.shape) # (1000209, 4)

print(data[0:5, 1]) # [1193  661  914 3408 2355]

mean_total = data[:, 2].mean()

print(mean_total) # 3.581564453029317
# 한 사람당 평균

user_ids = np.unique(data[:, 0]) # unique(겹쳐지는 내용은 무시하고 서로 다른 데이터만 출력)
print(user_ids) # [   1    2    3 ... 6038 6039 6040]

user_list = []

for user_id in user_ids:
    data_user = data[data[:, 0] == user_id, :] # 한사람당 모든 데이터
    mean_rating = data_user[:, 2].mean() # 각사람별 평점 평균
    user_list.append([user_id, mean_rating]) # 리스트에 아이디 평점 저장
print(user_list)
user_array = np.array(user_list, dtype = np.float)
np.savetxt("mean_rating_by_user.csv", user_array, fmt ="%.2", delimiter=",") # 콤마로 구분짓는 파일을 csv파일이라 한다.
np.savetxt("mean_rating_by_user.dat", user_array, fmt ="%.2", delimiter="::")
```

