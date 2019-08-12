# GUI01

```python
from tkinter import * # (*)모든 내용(안에 여러개 클래스 있으면 전부 사용)을 다 사용한다.

win = Tk() # Tk 객체 생성(윈도우)

b1 = Button(win, text="버튼1") # 버튼만들기
b1.pack() # 버튼 배치하기
b2 = Button(win, text="버튼2")
b2.pack()

win.mainloop() # (while) 반복 (x) 누르면 탈출

```

