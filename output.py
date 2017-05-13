from Tkinter import *

def f():
    global root
    root = Tk()
    root.title("Corrected paragraph")
    root.geometry('800x350+200+200')
    
    outp = open("out1.txt").read()
    labelText = StringVar()
    labelText.set('Corrected Paragraph')
    label1 = Label(root,textvariable = labelText, height = 4, fg="red4")
    label1.config(font=("Times New Roman", 20 ,"bold"))
    label1.pack()
    
    scrollbar=Scrollbar(root)
    scrollbar.pack(side=RIGHT,fill=Y)
    
    text=Text(root,width=150,wrap=WORD,bg='gray',yscrollcommand=scrollbar.set)
    text.insert(INSERT,outp)
    text.pack()

    scrollbar.config(command=text.yview)
    outp.close()
    root.mainloop()


