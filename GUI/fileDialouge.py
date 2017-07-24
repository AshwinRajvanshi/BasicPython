#Helps us to calcuate the size of the file.
##import Tkinter,tkFileDialog
##
##root = Tkinter.Tk()
##file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
##if file != None:
##    data = file.read()
##    file.close()
##    print "I got %d bytes from this file." % len(data)

#file Dialogue
from Tkinter import *
from tkFileDialog   import askopenfilename      

def callback():
    name= askopenfilename() 
    print name
    
errmsg = 'Error!'
Button(text='File Open', command=callback).pack(fill=X)
mainloop()
