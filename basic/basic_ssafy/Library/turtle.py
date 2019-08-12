import turtle

# 거북이가 놀 공간 (스크린)
# window = turtle.Screen()
# window.bgcolor("red")

# 꼬부기를 만들었다.
# ggobugi = turtle.Turtle()
# ggobugi.shape("turtle")
# ggobugi.color("yellow")

# 꼬부기를 발로찼다.
# ggobugi.forward(100)
# ggobugi.rt(90) # 각도를 숫자로 넣을 수 있다.

# for i in range(4):
#     ggobugi.forward(100)
#     ggobugi.rt(90)

# ggobugi.right(90) == ggobugi.rt(90)
# ggobugi.left(90) == ggobugi.lt(90)
    
# 클릭과 함께 윈도우를 끈다.
# window.exitonclick()

# 프로그램은 위에서부터 읽어오기 때문에 함수를 위에 작성한다.
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red") 

    ggobugi = turtle.Turtle()
    ggobugi.shape("turtle")
    ggobugi.color("yellow")

    onibugi = turtle.Turtle()
    onibugi.color("blue")
    onibugi.shape("turtle")
    
    # 사각형을 그려줘
    # draw_square(ggobugi)
    # draw_circle(onibugi)

    for _ in range(36):
        draw_circle(onibugi)
        onibugi.right(10)

    # 사각형을 그리고, 약간 틀어서 또 그리고
    for _ in range(36): # 특정 숫자만큼 단순반복을 할때 변수이름 대신 _ 를 쓴다.
        draw_square(ggobugi)
        ggobugi.right(10)



    # for i in range(4):
    #     ggobugi.forward(100)
    #     ggobugi.right(90)

    #     onibugi.circle(200)
    
    window.exitonclick()

def draw_square(character):
    for _ in range(4):
        character.forward(100)
        character.right(90)

def draw_circle(character):
    character.circle(75)


draw_art()