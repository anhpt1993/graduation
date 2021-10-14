from tkinter import *
from tkinter import messagebox as msg
from math import *
import matplotlib.pyplot as plt
import numpy as np

def check_input():
    try:
        a = float(entry_a.get()) if entry_a.get() != "" else 0
        b = float(entry_b.get()) if entry_b.get() != "" else 0
        c = float(entry_c.get()) if entry_c.get() != "" else 0
        if a != 0:
            return a, b, c
        else:
            msg.showwarning("CẢNH BÁO", "Giá trị 'a' phải khác 0")
    except ValueError:
        msg.showwarning("CẢNH BÁO","Kiểm tra lại dữ liệu đầu vào")

def run_program():
    a, b, c = check_input()
    delta = b**2 - 4 * a * c
    
    title_result.config(text = "+) Kết quả: ")
    # xoá các thông báo đã tồn tại trước đó
    announce1.config(text="")
    announce2.config(text="")
    announce3.config(text="")
    
    if delta < 0:
        announce1.config(text = "Phương trình vô nghiệm!!!")
        window.geometry("400x320")
    elif delta == 0:
        announce1.config(text = "Phương trình có một nghiệm kép!!!")
        announce2.config(text = f"x1 = x2 = {-b/2/a:.2f}")
        window.geometry("400x350")
    else:
        announce1.config(text="Phương trình có hai nghiệm riêng biệt!!!")
        announce2.config(text=f"x1 = {(-b-sqrt(delta))/2/a:.2f}")
        announce3.config(text=f"x2 = {(-b+sqrt(delta))/2/a:.2f}")
        window.geometry("400x380")
    draw_graph()

def cal_y(x):
    a, b, c = check_input()
    return a * (x ** 2) + b * x + c

def draw_graph():
    a, b, c = check_input()
    delta = b ** 2 - 4 * a * c

    # xác định toạ độ đỉnh
    x0 = -b / (2 * a)
    if delta > 0:
        x1 = (-b-sqrt(delta))/2/a
        x2 = (-b + sqrt(delta)) / 2 / a
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        avg_x = (max_x - min_x) / 2

    # Khởi tạo các toạ độ ban đầu
    if delta <= 0:
        x = np.arange(x0 - 5, x0 + 5.5, 0.5)
    else:
        x = np.arange(round(min_x - avg_x), round(max_x + avg_x), 0.1)
    y = []
    for i in x:
        y.append(cal_y(i))

    # phóng to, thu nhỏ đồ thị
    plt.figure(dpi = 150)

    # vẽ đồ thị y = 0
    if delta <= 0:
        x_ref = [x0 - 5, x0 + 5]
    else:
        x_ref = [round(min_x - avg_x), round(max_x + avg_x)]
    y_ref = [0, 0]

    plt.plot(x_ref, y_ref, "r--", label="y = 0")

    # vẽ đồ thị y =  ax^2 + bx + c
    plt.plot(x, y, "b-", label=f"y = {a}x^2 + {b}x + {c}")

    plt.title("Graph", fontdict={"fontname": "calibri", "fontsize": 20})
    plt.xlabel("X Axis", fontdict={"fontname": "Comic Sans MS"})
    plt.ylabel("Y Axis", fontdict={"fontname": "Comic Sans MS"})

    if delta <= 0:
        x_tick = [round(x[0]), x0, round(x[len(x) - 1])]
    else:
        x_tick = [round(min_x - avg_x), round(min_x), round(min_x + avg_x), round(max_x), round(max_x + avg_x)]

    plt.xticks(x_tick)
    # plt.yticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])

    plt.legend()

    plt.show()


window = Tk()
window.geometry("400x250")
window.title("Basic Mathematics")
window.resizable(0, 0)
icon = PhotoImage(file="logo.png")
window.iconphoto(True, icon)

# đưa ảnh chứa biểu thức vào trong window
img_format = PhotoImage(file="formula.png")
Label(window, image = img_format).place(x = 50, y = 10)

# tạo nhãn "Nhập giá trị"
title_input = Label(window, text = "+) Nhập giá trị: ", font = ("calibri", 16, "bold"))
title_input.place(x = 5, y = 50)
# tạo nhãn và entry "a":
label_a = Label(window,
                text = "a",
                font = ("calibri", 16, "bold"))
label_a.place(x = 50, y = 80)
entry_a = Entry(window,
                width = 5,
                font = ("calibri", 14))
entry_a.place(x = 30, y = 110)

# tạo nhãn và entry "b":
label_b = Label(window,
                text = "b",
                font = ("calibri", 16, "bold"))
label_b.place(x = 200, y = 80)
entry_b = Entry(window,
                width = 5,
                font = ("calibri", 14))
entry_b.place(x = 180, y = 110)

# tạo nhãn và entry "c":
label_c = Label(window,
                text = "c",
                font = ("calibri", 16, "bold"))
label_c.place(x = 350, y = 80)
entry_c = Entry(window,
                width = 5,
                font = ("calibri", 14))
entry_c.place(x = 330, y = 110)

# tạo nút bấm thực thi
btn_photo = PhotoImage(file = "arrow-down.png")
Label(window, image = btn_photo).place(x = 168, y = 150)
btn_execute = Button(window, text = "SOLVING!!!", command = run_program)
btn_execute.place(x = 165, y = 220)

# tạo nhãn kết quả
title_result = Label(window, text = "", font = ("calibri", 16, "bold"))
title_result.place(x = 5, y = 250)

announce1 = Label(window, text = "", font = 14)
announce1.place(x = 25, y = 280)

announce2 = Label(window, text = "", font = 14)
announce2.place(x = 25, y = 310)

announce3 = Label(window, text = "", font = 14)
announce3.place(x = 25, y = 340)

window.mainloop()