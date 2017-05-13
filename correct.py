from Tkinter import *
#from finalbasic import *


def fun3():
    global rep
    rep  = ''
    root.destroy()
    
def fun2(r):
    global root
    global rep
    rep = r
    root.destroy()


def fun1(sentence,matches):
    global root,rep
    root = Tk()
    root.title("Language Translation Identification")
    root.geometry('800x450+200+200')

    labelText = StringVar()
    labelText.set('Error Sentence')
    label1 = Label(root,textvariable = labelText, height = 2, fg="red4")
    label1.config(font=("Times New Roman", 20 ,"bold"))
    label1.pack()
    labeltext1 = StringVar()
    labeltext1.set(sentence)
    label2 = Label(root,justify = LEFT, compound = LEFT, textvariable = labeltext1,fg="blue")
    label2.pack()
    
    labeltext2 = StringVar()
    labeltext2.set('Error: "'+sentence[matches[0].fromx:matches[0].tox]+'" at position '+str(matches[0].fromx)+' to '+str(matches[0].tox))
    label3 = Label(root,justify = LEFT,compound = LEFT,textvariable = labeltext2,fg="blue")
    label3.pack()

    labeltext3 = StringVar()
    labeltext3.set('Enter Correction: ')
    label4 = Label(root, justify = LEFT, textvariable = labeltext3)
    label4.config(font=('Times',10,'bold'))
    label4.pack()
    
    E = Entry(root, exportselection=0, justify='center',bd=0)
    E.pack(padx=100, pady=10, expand=0, fill='x')

    labeltext4 = StringVar()
    labeltext4.set('Suggestion')
    label5 = Label(root, justify = LEFT, textvariable = labeltext4)
    label5.config(font=('Times',10,'bold'))
    label5.pack()

    #labeltext5 = StringVar()
    #labeltext5.set(matches[0])
    #label6 = Label(root,justify = LEFT, compound = LEFT, textvariable = labeltext5,fg="red")
    label6 = Text(root, width = 50, height = 10, wrap = WORD)
    label6.insert(INSERT,matches[0])
    label6.pack()
    
    b1 = Button(root, text = 'Correct', command = lambda: fun2(E.get())).pack()
    b2 = Button(root, text = 'Auto Correct', command = fun3).pack()
    #rep = E.get()
    root.mainloop()
    return rep
