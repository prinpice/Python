# pygame04

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
# 2번 큰네모를 하나 더 만든다.
# 1번 네모가 2번네모랑 충돌하면 작은 네모가 2번네모로 이동하고 그 다음부터는 2번네모가 조종
rc_x1 = 100
rc_y1 = 100
rc_w1 = 50
rc_h1 = 50
rc_x2 = 300
rc_y2 = 100
rc_w2 = 50
rc_h2 = 50
count = 0

end = False
while end == False:
    for event in pygame.event.get(): # pygame.event 에 모든 정보가 들어온다.
        if event.type == pygame.QUIT: # event 가 x 버튼 눌렀다면
            end = True
        if event.type == pygame.KEYDOWN:  # 아무거나 눌렀다면
            if event.key == pygame.K_RIGHT:
                rc_x1 += 10
            if event.key == pygame.K_LEFT:
                rc_x2 -= 10
        if event.type == pygame.KEYUP:
            pass

    # ====================update========================
    # ====================render========================
    screen.fill((r, g, b)) # 배경 색 변경
                    # ( 부모, 컬러, (위치, 크기))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect((rc_x1, rc_y1), (rc_w1, rc_h1)))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect((rc_x2, rc_y2), (rc_w2, rc_h2)))
    # 수정필요
    if count % 2 == 0:
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect((rc_x1 + 10, rc_y1 + 10), (rc_w1 - 20, rc_h1 - 20)))
    else:
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect((rc_x2 + 10, rc_y2 + 10), (rc_w2 - 20, rc_h2 - 20)))
    if rc_x2 == rc_x1 + rc_w1:
        pygame.draw.rect(screen, (255, 100, 0), pygame.Rect((rc_x2 + 10, rc_y2 + 10), (rc_w2 - 20, rc_h2 - 20)))
        count += 1

    pygame.display.flip() # 화면을 다 지우고 다시 그린다.
    clock.tick(60) # 초당 60 프레임 (사람 눈을 속일 수 있다.)




# =============================================
pygame.quit()





```

