# from tkinter import *
# from tkinter import messagebox

# def clickLeft(event):
#     messagebox.showinfo("마우스", "마우스 왼쪽 더블 버튼이 클릭됨")

# window = Tk()

# window.bind("<Double-Button-1>", clickLeft)

# window.mainloop()

# from tkinter import *


# def clickMouse(event) :
#     txt = ""
#     if event.num == 1 :
#         txt += "마우스 왼쪽 버튼이 ("
#     elif event.num == 3 :
#         txt += "마우스 오른쪽 버튼이 ("

#     txt += str(event.y) + ", " + str(event.x) + ")에서 클릭됨"
#     label1.configure(text = txt)


# window = Tk()
# window.geometry("400x400")

# label1 = Label(window, text = "아~~~~~ 자고 싶다~~~~~")

# window.bind("<Button>", clickMouse)

# label1.pack(expand = 1, anchor = CENTER)
# window.mainloop()


# from tkinter import *
# from tkinter import messagebox



# def keyEvent(event):
#     messagebox.showinfo("키보드 이벤트", "눌린 키 : " + chr(event.keycode))



# window = Tk()

# window.bind("<Alt,L>", keyEvent)

# window.mainloop()

from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    messagebox.showinfo("키보드 이벤트", "눌린 키 : Shift + " + event.keysym)

window = Tk()

window.bind("<Shift-Left>", keyEvent)
window.bind("<Shift-Up>", keyEvent)
window.bind("<Shift-Right>", keyEvent)
window.bind("<Shift-Down>", keyEvent)

window.mainloop()