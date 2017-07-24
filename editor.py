from Tkinter import *
import tkMessageBox
import Tkinter
import tkFileDialog

def donothing():
   print "a"

def file_save():
    name=asksaveasfile(mode='w',defaultextension=".txt")
    text2save=str(text.get(0.0,END))
    name.write(text2save)
    name.close

root = Tk()
root.geometry("500x500")
menubar=Menu(root)
text=Text(root)
text.pack()
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
