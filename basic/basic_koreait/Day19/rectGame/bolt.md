# bolt

```python
import pygame
from Day19.rectGame.rect import RECT

class Bolt:



    def __init__(self, x, y):
        self.bolt = RECT(x, y, 20, 20)

    def movement(self):
        self.bolt.left += 10
        self.bolt.right += 10

    def render(self, screen):
        self.bolt.render(screen)
```

