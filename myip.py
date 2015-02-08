#!/usr/bin/python

#Author: Justin Clark
#name: ipgui.py
#function: opens a window returning ip address

import urllib
import re
from Tkinter import *
#import Tkinter


def ipCheck():
    data = urllib.urlopen('http://checkip.dyndns.org').read()
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip = re.search(pattern, data).group()
    root = Tk()
    ipWindow = Label(root, text='\n\tYour IP Address is: ' + ip + '\t\n')
    ipWindow.pack()
    return ip


class App:
    def __init__(self, parent):
        #The frame instance is stored in a local variable 'f'.
        #After creating the widget, we immediately call the
        #pack method to make the frame visible.

        f = Frame(parent)
        f.pack(padx=15, pady=15)

        self.button = Button(f, text="IP", command=ipCheck)
        self.button.pack(side=BOTTOM, padx=10, pady=10)

        self.exit = Button(f, text="exit", command=f.quit)
        self.exit.pack(side=BOTTOM, padx=10, pady=10)

root = Tk()
root.title('ipgui')
app = App(root)

root.mainloop()
