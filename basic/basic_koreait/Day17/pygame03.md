# pygame03

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
# 문제 1)큰 네모 안에 작은 네모 그리기
# 문제 2) 큰 네모가 좌우로 움직일수 있게
# 문제 3) 큰 네모가 좌우로 움직일 떄 작은 네모가 큰 네모를 벗어날 수 없게
rc_x = 100
rc_y = 100
rc_w = 50
rc_h = 50
end = False
while end == False:
    for event in pygame.event.get(): # pygame.event 에 모든 정보가 들어온다.
        if event.type == pygame.QUIT: # event 가 x 버튼 눌렀다면
            end = True
        if event.type == pygame.KEYDOWN:  # 아무거나 눌렀다면
            if event.key == pygame.K_RIGHT: # 그 키가 숫자 1 이면
                rc_x += 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                pass

    # ====================update========================
    # ====================render========================
    screen.fill((r, g, b)) # 배경 색 변경
                    # ( 부모, 컬러, (위치, 크기))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((rc_x, rc_y), (rc_w, rc_h)))
    pygame.draw.rect(screen, (255,100, 0), pygame.Rect((rc_x + 10, rc_y + 10), (rc_w - 20, rc_h - 20)))
    pygame.display.flip() # 화면을 다 지우고 다시 그린다.
    clock.tick(60) # 초당 60 프레임 (사람 눈을 속일 수 있다.)




# =============================================
pygame.quit()




# 2번 큰네모를 하나 더 만든다.
# 1번 네모가 2번네모랑 충돌하면 작은 네모가 2번네모로 이동하고 그 다음부터는 2번네모가 조종
```

