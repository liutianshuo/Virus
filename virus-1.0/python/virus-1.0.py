# -*- coding: UTF-8 -*-

# 这是由开发者 Liu Tianshuo 于 12 岁时开发的一个恶搞程序
# 版本 1.0
# 程序仅为恶搞，结束该程序进程（如重启、使用任务管理器终止等）即可消除本程序对电脑的一切影响

import Play_mp3 # 引用播放音乐的库
import webbrowser # 引用使用浏览器打开指定网址的库
import tkinter # 引用弹出弹窗的库
import tkinter.messagebox # 引用弹出弹窗的库
from threading import Thread # 引用多线程执行命令的库

# 弹出信息弹窗
tkinter.messagebox.showinfo('Virus','嗨嗨嗨！')
tkinter.messagebox.showinfo('Virus','我很高兴，你的电脑马上就要无了。')
tkinter.messagebox.showinfo('Virus','准备好了吗？')
tkinter.messagebox.showinfo('Virus','尽情欣赏吧！')
tkinter.messagebox.showinfo('Virus','三、二、一、开始！')

# 无限浏览器打开窗口
def aa():
    while True:
        webbrowser.open("liutianshuo.cn")

# 无限播放音乐
def ab():
    while True:
        Play_mp3.play("https://software-resources.oss-cn-beijing.aliyuncs.com/virus/virus-1.0/music-1.mp3")

# 无限计算 114514、1919810 进行各种数学运算后的结果（悲）
def ac():
    while True:
        a = 114514
        b = 1919810
        c = a + b
        d = a - b
        e = a * b
        f = a / b
        g = a ** b
        h = a // b
        i = a % b
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
        print(i)

# 同时执行无限浏览器打开窗口、无限播放音乐、无限计算 114514、1919810 进行各种数学运算后的结果三个进程
if __name__ == '__main__':
    Thread(target = aa).start()
    Thread(target = ab).start()
    Thread(target = ac).start()