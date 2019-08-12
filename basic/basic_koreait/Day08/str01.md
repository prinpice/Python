# str01

```python
import datetime # 날짜관련

today = datetime.date.today()
print(today) # 2018-04-19 문자 아님

# 문제 1) 2018년 04월 19일로 출력해보세요

# print(today[0:4], "년") # TypeError: 자를수가 없다.
st1 = "korea"
print(st1[0:4])

# 타입확인 ==> type(변수)
print(type(st1))
print(type(today))

# 타입 변환 ==> 형변환 ==> casting
today = str(today)
print(today[0:4]) # <class 'str'>

# 문제 1) 2018년 04월 19일로 출력해보세요
print(today[0:4], "년", today[5:7], "월", today[8:10], "일")

yy = today[0:4]
mm = today [5:7]
dd = today[8:] # 끝까지
print(yy, "년", mm, "월", dd, "일") # 2018 년 04 월 19 일

```

