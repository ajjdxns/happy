import tkinter as tk
import random
root = tk.Tk()
with open (r"D:\文件\编程\python\程序\项目\happy\name.txt") as f:
    name = f.read()
    who = name.split("\n")
with open (r"D:\文件\编程\python\程序\项目\happy\location.txt") as f:
    location = f.read()
    where = location.split("\n")
with open (r"D:\文件\编程\python\程序\项目\happy\doing.txt") as f:
    doing = f.read()
    do = doing.split("\n")
def run():
    label['text'] = "{}在{}{}".format(random.choice(who),random.choice(where),random.choice(do))
label = tk.Label(root, text="按下按钮生成笑话")
button = tk.Button(root, text="start",command=run)
label.pack()
button.pack()
root.mainloop()