import os

def Cls():
    os.system("cls")
Cls()

import tkinter as tk

win = tk.Tk()

Width = 750
Height = 50
Margin_top = 50
margin_left = 100
win.geometry(f"{Width}x{Height}+{margin_left}+{Margin_top}")
win.config(background="#1E1E1E")
win.title("Main")

def f_button1():
    win_button1 = tk.Tk()
    import wifi_pass
    x = wifi_pass.Wifi()
    x.f_wifi_name("Netsh wlan show profile")

    button1_label1 = tk.Label(win_button1, text=x)
    button1_label1.pack()

    win_button1.mainloop()
button1 = tk.Button(win, text="Your Wifi Pass",
                            width=20,
                            height=2,
                            command=f_button1
                            )
button1.pack(side=["left"])

button2 = tk.Button(win, text="test2",
                            width=20,
                            height=2
                            )
button2.pack(side=["left"])

button3 = tk.Button(win, text="test3",
                            width=20,
                            height=2
                            )
button3.pack(side=["left"])

button4 = tk.Button(win, text="test4",
                            width=20,
                            height=2
                            )
button4.pack(side=["left"])

button5 = tk.Button(win, text="test5",
                            width=20,
                            height=2
                            )
button5.pack(side=["left"])

win.mainloop()