import sys
from Tkinter import *
#from basic import *

def getfname():
    global E, fname
    fname = E.get()
    print fname
    main()
    
def main():
    print "File name received."
    root.destroy()

root = Tk()
root.config(height = 500, width = 670, background = '#888888')
fname = StringVar()
L = Label(root, textvariable = fname, height = 3, width = 100, background = '#888888')
fname.set("Langauge check: Enter file name")
L.pack()
E = Entry(root, exportselection=0, justify='center',bd=0)
E.pack(padx=100, pady=10, expand=0, fill='x')
b1 = Button(root, text='Go!')
b1.config(height = 2, width = 5, command=getfname)
b1.pack()
root.mainloop()
