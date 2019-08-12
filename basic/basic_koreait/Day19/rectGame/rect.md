# rect

```python
import pygame


class RECT:
    def __init__(self, left, top, wid, height):
        self.left = left
        self.top = top
        self.right = left + wid
        self.bottom = top + height
        self.wid = wid
        self.height = height
        self.red = 255
        self.green = 255
        self.blue = 255

    def render(self, screen):
        pygame.draw.rect(screen, (self.red, self.green, self.blue),
                         pygame.Rect((self.left, self.top), (self.wid, self.height)))

```

