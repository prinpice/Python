# str02

```python
# 1. 여러줄 표현하기
print("hello python "
      "hello java") # hello python hello java

print("""
hello python
hello java""")
print('''
hello python
hello java''') # 파이썬은 홑따옴표 '', 쌍따옴표 ""를 구분하지 않는다.
# hello python
# hello java

# 이스케이프 문자 (escape)
"""
\n   : 문자열 안에서 줄을 바꾸고 싶을 때 사용 (new line)
\t   : 문자열 사이에서 간격을 줄 때 사용 (tab)
\\   : 문자 \ 를 표현하고 싶을 떄 사용
\'   : 홑따옴표를 표현할 때 사용
\"   : 쌍따옴표를 표현할 때 사용
"""
print("안녕\n하세요")
print("반갑\t습니다") # 반갑 습니다
print("hello \\ python") # \ 자체가 기능이기 떄문에 두개를 사용해서 문자표기를 한다.
print("hello \" java") # hello " java
```

