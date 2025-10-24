#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python 的 GUI 并没有操作系统原生的GUI编程那么好用
# 但是比Java好，目前还是推荐Java的 B/S 模式

from tkinter import *

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


def start():
    app = Application()
    app.master.title('Hello python')
    app.mainloop()

if __name__ == '__main__':
    start()