# pygame01

```python
import pygame

# 1. 프레임(60: 초당 60번 프로그램이 돌아가는것): 사람 눈 속이기에 60이면 충분(30도 가능) 2. 윈도우 좌표(x, y) 3. 이벤트
pygame.init()
# =============================================
size_x = 1000
size_y = 500
screen = pygame.display.set_mode((size_x, size_y)) # window 창 사이즈

r = 255 # 0~ 255
g = 255
b = 0
clock = pygame.time.Clock() # 파이게임에서 제공하는 시간관련 클래스
# 1. 초기화 2. 연산(계산) 3. 그리기

# 1을 누르고 있으면 색이 변하고 떼면 변하지 않음
isRed = False # True(1), False(0)
end = False
while end == False:
    for event in pygame.event.get(): # pygame.event 에 모든 정보가 들어온다.
        if event.type == pygame.QUIT: # event 가 x 버튼 눌렀다면
            end = True
        if event.type == pygame.KEYDOWN:  # 아무거나 눌렀다면
            if event.key == pygame.K_1: # 그 키가 숫자 1 이면
                isRed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                isRed = False

    # ====================update========================
    if isRed == True:
        r -= 1
    if r == 0:
        r = 255
    # ====================render========================
    screen.fill((r, g, b)) # 배경 색 변경
    pygame.display.flip() # 화면을 다 지우고 다시 그린다.
    clock.tick(60) # 초당 60 프레임 (사람 눈을 속일 수 있다.)




# =============================================
pygame.quit()
```

