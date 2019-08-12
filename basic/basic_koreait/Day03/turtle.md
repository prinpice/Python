# turtle

```python
import turtle # turtle 이라는 파일을 추가한다. 모듈
import math
turtle.shape("turtle") # 거북이를 그린다.
#========================================================
"""
turtle.forward(100) # 전진
turtle.lt(120) # 좌회전
turtle.forward(100) # 전진

turtle.up() # 꼬리를 든다 ==> 꼬리에 잉크가 묻어있는데 꼬리를 들어서 그림이 안그려진다
turtle.forward(100) # 전진
turtle.forward(100) # 전진

turtle.down() # 꼬리를 다시 내린다 ==> 그림이 다시 그려진다
turtle.dorward(100) # 전진

turtle.circle(200) # 숫자 사이즈의 동그라미를 그린다

# 문제 1) 이름을 그려보세요

#========================================
turtle.exitonclick() # 클릭하면 종료된다.
"""
turtle.up()
turtle.lt(90)
turtle.forward(100)
turtle.lt(90)
turtle.forward(300)
turtle.lt(180)
turtle.down()

a = math.sqrt(2)
turtle.forward(100)
turtle.rt(135)
turtle.forward(100*a)
turtle.lt(180)
turtle.forward(50*a)
turtle.rt(90)
turtle.forward(50*a)
turtle.lt(135)

turtle.up()
turtle.forward(50)
turtle.rt(90)
turtle.down()
turtle.forward(50)
turtle.lt(90)
turtle.forward(50)
turtle.lt(180)
turtle.forward(100)
turtle.up()
turtle.rt(90)
turtle.forward(75)
turtle.lt(90)
turtle.forward(50)
turtle.down()
turtle.circle(30)

turtle.up()
turtle.rt(180)
turtle.forward(175)
turtle.rt(90)
turtle.forward(175)

turtle.down()
turtle.rt(45)
turtle.forward(25)
turtle.rt(135)
turtle.forward(50)
turtle.rt(180)
turtle.forward(100)
turtle.rt(135)
turtle.forward(100*a)
turtle.rt(180)
turtle.forward(50*a)
turtle.rt(90)
turtle.forward(50*a)

turtle.up()
turtle.lt(45)
turtle.forward(25)
turtle.lt(90)
turtle.down()
turtle.forward(100)
turtle.rt(180)
turtle.forward(50)
turtle.lt(90)
turtle.forward(50)
turtle.lt(180)
turtle.forward(50)
turtle.lt(90)
turtle.forward(50)

turtle.up()
turtle.forward(25)
turtle.rt(90)
turtle.forward(75)
turtle.lt(90)
turtle.down()
turtle.forward(50)
turtle.lt(90)
turtle.forward(100)

turtle.up()
turtle.lt(90)
turtle.forward(150)
turtle.rt(90)
turtle.forward(50)
turtle.down()
turtle.forward(100)
turtle.rt(90)
turtle.forward(100)
turtle.rt(90)
turtle.forward(100)
turtle.rt(90)
turtle.forward(100)

turtle.up()
turtle.forward(25)
turtle.rt(90)
turtle.forward(150)
turtle.rt(90)
turtle.down()
turtle.forward(150)


turtle.exitonclick()
```

