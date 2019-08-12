# GUI03

```python
from tkinter import *
"""
StrungVar()
IntVar()
DoubleVar()
BooleanVar()
"""
win = Tk()

str1 = StringVar()
str1.set("버튼1") # ( str1 = "버튼1" ) 과 같다


def print_msg():
    print("현재 클릭된 버튼: ", str1.get()) # (str1.get)은 (str1)과 같다.




b1 = Button(win,text = "버튼1", command = print_msg)
b1.grid(row = 0, column = 0, padx= 0, pady =0)
b2 = Button(win, text = "버튼2")
b2.grid(row=1, column=1, padx=10, pady = 10)



win.mainloop() # (while) 반복 (x) 누르면 탈출
```

