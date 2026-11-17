from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


# 함수 선언 부분
def func_open():
    filepath = askopenfilename(
        title="gif 이미지 오픈",
        filetypes=(("gif이미지", "*.gif"), ("모든 파일", "*.*"))
    )

    if filepath:
        tk_img = PhotoImage(master=window, file=filepath)

        image_label.config(image=tk_img)
        image_label.image = tk_img


def func_exit():
    window.quit()
    window.destroy()


# 메인 코드 부분
window = Tk()
window.title("GIF 화면")
window.geometry("600x500")

image_label = Label(window)
image_label.pack()


mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

viewMenu = Menu(mainMenu)
mainMenu.add_cascade(label="보기", menu=viewMenu)
viewMenu.add_command(label="축소", command=func_open)
viewMenu.add_separator()
viewMenu.add_command(label="확대", command=func_exit)

homeMenu = Menu(mainMenu)
mainMenu.add_cascade(label="홈", menu=homeMenu)
homeMenu.add_command(label="저장", command=func_open)
homeMenu.add_separator()
homeMenu.add_command(label="선택", command=func_exit)
homeMenu.add_separator()
homeMenu.add_command(label="찾기", command=func_exit)


window.mainloop()