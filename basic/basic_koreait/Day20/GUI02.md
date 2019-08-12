# GUI02

```python
from tkinter import *

win = Tk()

b1 = Button(win,text = "버튼1")
b1.grid(row = 0, column = 0, padx= 0, pady =0)
b2 = Button(win, text = "버튼2")
b2.grid(row=1, column=1, padx=10, pady = 10)
win.mainloop() # (while) 반복 (x) 누르면 탈출
```

