# from tkinter import *

# window = Tk()

# btnList = [None] * 3

# for i in range(0, 3):
#     btnList[i] = Button(window, text = "버튼" + str(i + 1))

# for btn in btnList:
#     btn.pack(side = TOP, fill = X, ipadx = 10, padx = 10, pady =10  )

# window.mainloop()



# from tkinter import *



# btnList = [None] * 9

# fnameList = ["Fau.gif", "ish.gif", "Rosu.gif", "Roza.gif",
#              "Yi.gif", "hong.gif", "Gre.gif", "Outis.gif", "Heath.gif"]

# photoList = [None] * 9

# i, k = 0, 0

# xPos, yPos = 0, 0

# num = 0
# window = Tk()
# window.title("JPG 이미지 불러오기")
# window.geometry("210x210")

# for i in range(0, 9):
#     photoList[i] = PhotoImage(file = "C:/Users/Admin/Documents/20261448_is_python/python/gif/" + fnameList[i])
#     btnList[i] = Button(window, image = photoList[i])

# for i in range(0, 3):
#     for k in range(0, 3):
#         btnList[num].place(x = xPos, y = yPos)
#         num += 1
#         xPos += 70
#     xPos = 0
#     yPos += 70

# window.mainloop()

import tkinter as tk
from PIL import Image, ImageTk, ImageOps

# --- 윈도우 창 설정 ---
window = tk.Tk()
window.title("JPG 이미지 불러오기")
window.geometry("200x200")

# 1. JPG 이미지 경로 설정 (확장자가 .jpg 또는 .jpeg인지 확인)
image_path = r"C:\Users\Admin\Downloads\images.jpg"

# 이미지 열기
image = Image.open(image_path)