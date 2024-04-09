#!/usr/bin/python


import os, sys
from tkinter import *
import tkinter
from tkinter import messagebox
import tkinter as tk
import re
from os.path import exists
from PIL import Image

top = tkinter.Tk()
top.title("Modify size img (© F.Steven) V 1.0.3")
top.geometry('450x150')


def Check():
    filename = E1.get()
    filename2 = E2.get()
    try:
        sizex = int(E6.get())
        sizey = int(E7.get())

        if(exists(filename)):
            if(exists(filename2)):

                path = filename+"/"
                path2= filename2+"/"
                dirs = os.listdir( path )
                for item in dirs:
                    if os.path.isfile(path+item):
                        im = Image.open(path+item)
                        f, e = os.path.splitext(path+item)
                        imResize = im.resize((sizex,sizey), Image.ANTIALIAS)
                        try:
                            imResize.save(path2+item, 'JPEG', quality=90)
                        except:
                            imResize.save(path2+item, 'PNG', quality=90)

                L3 = Label(top, text= "Edited         \nsuccessfully        " , fg="red",anchor='w',justify=LEFT)
                L3.pack( padx = 50, pady = 5)
                L3.place ( x = 170, y = 90)

            else:
                L3 = Label(top, text= "Output folder  \ndoes not exist      " , fg="red",anchor='w',justify=LEFT)
                L3.pack( padx = 50, pady = 5)
                L3.place ( x = 170, y = 90)
        else:
            L3 = Label(top, text=     "Input folder   \ndoes not exist      " , fg="red",anchor='w',justify=LEFT)
            L3.pack( padx = 50, pady = 5)
            L3.place ( x = 170, y = 90)
    except:
        L3 = Label(top, text=         "Invalid size or\n  invalid file        " , fg="red",anchor='w')
        L3.pack( padx = 50, pady = 5)
        L3.place ( x = 170, y = 90)



#label
L1 = Label(top, text="Insert folder input:")
L1.place ( x = 10, y = 5)
#entry
E1 = Entry(top, bd =2)
E1.place(x = 10, y = 35)

#bottone
b = tkinter.Button(top, text= "Resize image\n in folder",bd =4 , command = Check)
b.place(x = 170, y = 30)

#label2
L2 = Label(top, text="Insert folder output:")
L2.place ( x = 10, y = 70)

#entry
E2 = Entry(top, bd =2)
E2.place(x = 10, y = 100)

#labe3
L6 = Label(top, text="Set size in X")
L6.place ( x = 290, y = 5)
#entry
E6 = Entry(top, bd =2)
E6.place(x = 290, y = 35)

#label4
L7 = Label(top, text="Set size in Y")
L7.place ( x = 290, y = 70)

#entry
E7 = Entry(top, bd =2)
E7.place(x = 290, y = 100)

def quit():
    top.destroy()
    sys.exit()

#quit
top.protocol('WM_DELETE_WINDOW', quit)

#loop
top.mainloop()
