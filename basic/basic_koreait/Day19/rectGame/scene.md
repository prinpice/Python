# scene

```python
import pygame
import random
from Day19.rectGame.rect import RECT
from Day19.rectGame.bolt import Bolt



class Scene:
    def __init__(self):
        self.rc = RECT(200, 200, 80, 80)
        self.count = 0
        self.boltManager = []

    def update(self):
        self.count += 1
        if self.count % 10 == 0:
            self.rc.red = random.randint(0, 255)
            self.rc.green = random.randint(0, 255)
            self.rc.blue = random.randint(0, 255)
        for i in self.boltManager:
            i.movement()

    def render(self, screen):

        self.rc.render(screen)
        for i in self.boltManager:
            i.render(screen)




    def key_setting(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.rc.left += 10
                self.rc.right += 10
            if event.key == pygame.K_SPACE:
                self.boltManager.append(Bolt(self.rc.left, self.rc.top))
```

