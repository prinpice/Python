# class02

```python
# 상속
"""
객체 지향의 가장 큰 장점은 코드의 재활용

1. 클래스를 여러개 사용하는 경우: 겹치는 멤버(클래스 내부 def 내부에 있는 것들) 들을 상속을 통해서 간결하게 만들 수 있다.
2. 상속해주는 클래스를: 부모클래스
3. 상속받는 클래스는 : 자식클래스

상속하는법
class 자식클래스이름(부모클래스이름):
"""


class Player:
    def __init__(self):
        self.hp = 0 # 멤버
        self.pow = 0
        self.armor = 0
        self.weapon = 0
        self.magic = 0
        self.name = ""
class Monster:
    def __init__(self):
        self.hp = 0
        self.pow = 0
        self.armor = 0
        self.weapon = 0
        self.name = ""

class Monster1:
    def __init__(self):
        self.hp = 0  # 멤버
        self.pow = 0
        self.armor = 0
        self.weapon = 0
        self.magic = 0
        self.name = ""
# 몬스터가 100마리 등 많으면 비효율적

```

