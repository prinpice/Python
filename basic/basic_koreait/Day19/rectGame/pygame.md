# pygame

```python
import pygame
from Day19.rectGame.scene import Scene # 경로설정 + 파일암포트
pygame.init()


screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock() # 60프레임으로 설정(불필요한 연산 줄이기 위해)

end = False
scene = Scene()
while not end: # 무한반복
    for event in pygame.event.get(): # 모든 이벤트가 저장된다.
        if event.type == pygame.QUIT: # x 버튼을 눌렀다면
            end = True
        scene.key_setting(event) # 내 윈도우에 붙이기 위해 event 넣어줌
    # ===================== update =============================
    scene.update()


    # ==========================================================
    screen.fill((255, 255, 0)) # 0 ~ 255

    scene.render(screen) # 내 윈도우에 그리기 위해 screen 넘겨줌

    pygame.display.flip() # 지우고 다시 그리기

    clock.tick(60) # 초당 60 프레임



pygame.quit()
```

