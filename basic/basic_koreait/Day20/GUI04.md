# GUI04

```python
from tkinter import *

class App1:
    def __init__(self, win):
        self.n1 = IntVar()
        self.n2 = IntVar()
        self.sum = IntVar()
        Label(win, text = "숫자1").grid(row = 0, column = 0) # 글만 써있는 위젯 ( 버튼같은 오브젝트를 위젯이라고 한다.)
        Label(win, text = "숫자2").grid(row = 1, column = 0)
        Label(win, text = "결과").grid(row = 2, column = 0)
        self.e1 = Entry(win, textvariable= self.n1) # 글을 적을 수 있는 위젯: 글이 n1에 저장
        self.e1.grid(row = 0, column = 1)
        self.e2= Entry(win, textvariable = self.n2)
        self.e2.grid(row = 1, column = 1)
        self.result = Entry(win, textvariable = self.sum)
        self.result.grid(row = 2, column = 1)
        self.b1 = Button(win, text= "더하기", command=self.cal_sum)
        self.b1.grid(row = 2, column = 2)
    def cal_sum(self):
        a = self.n1.get()
        b = self.n2.get()
        c = a + b
        self.sum.set(c)
        print(c)
win = Tk()
app1 = App1(win)
win.mainloop()
```

