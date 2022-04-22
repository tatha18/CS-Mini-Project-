import tkinter
from tkinter import *
import random
root=tkinter.Tk()
root.title("QUIZZER")
root.geometry("700x700")
root.config(background="light blue")
labeltexter= Label(root,bg="light blue", text="QUIZZER", font=("monospace",32,"bold") )
labeltexter.pack(pady=(70,0))
def quizstart():
    labeltexter.destroy()
    labeltexter1.destroy()
    labeltexter3.destroy()
    lblrulez.destroy()
    buttony.destroy()
    q1()
    q2()
    q3()
    q4()


def q1():
    l1=Label(root,text="Who is the Current President of India?",font=("monospace",22,"bold"))
    l1.pack()
    r1= Radiobutton(root,bg="light blue",text="Narendra Modi", font=("monospace",12), value=0,variable=2)
    r1.pack()
    r2= Radiobutton(root,bg="light blue",text="Ram Nath Kovind", font=("monospace",12), value=1,variable=3)
    r2.pack()
    r3= Radiobutton(root,bg="light blue",text="Christian Horner", font=("monospace",12), value=2,variable=4)
    r3.pack()
def q2():
    l1=Label(root,text="Who is the World's greatest Formula 1 driver?",font=("monospace",22,"bold"))
    l1.pack(pady=(30,0))
    r4= Radiobutton(root,bg="light blue",text="Vettel", font=("monospace",12), value=3,variable=5)
    r4.pack()
    r5= Radiobutton(root,bg="light blue",text="Hamilton ", font=("monospace",12), value=4,variable=6)
    r5.pack()
    r6= Radiobutton(root,bg="light blue",text="Mazepin", font=("monospace",12), value=5,variable=7)
    r6.pack()
def q3():
    l1=Label(root,text="What is the capital of Utah?",font=("monospace",22,"bold"))
    l1.pack(pady=(70,0))
    r7= Radiobutton(root,bg="light blue",text="Salt Lake City", font=("monospace",12), value=6,variable=8)
    r7.pack()
    r8= Radiobutton(root,bg="light blue",text="Colorado", font=("monospace",12), value=7,variable=9)
    r8.pack()
    r9= Radiobutton(root,bg="light blue",text="Denver", font=("monospace",12), value=8,variable=10)
    r9.pack()
def q4():
    l1=Label(root,text="Who built Python?",font=("monospace",22,"bold"))
    l1.pack(pady=(110,0))
    r10= Radiobutton(root,bg="light blue",text="Toto Wolff", font=("monospace",12), value=9,variable=11)
    r10.pack()
    r11= Radiobutton(root,bg="light blue",text="Guido Rossum ", font=("monospace",12), value=10,variable=12)
    r11.pack()
    r12= Radiobutton(root,bg="light blue",text="Guenther Steiner", font=("monospace",12), value=11,variable=13)
    r12.pack()
labeltexter1= Label(root,bg="light blue", text="Click the button below to start your quiz", font=("monospace",22,"bold") )
labeltexter1.pack(pady=(90,0))
labeltexter3= Label(root,bg="light blue", text="Don't cheat and all the best!", font=("monospace",16,"italic") )
labeltexter3.pack(pady=(100,0))

buttony= Button(root,bg="green",width="10",height="2", text="Start",command=quizstart)
buttony.pack(pady=(95,0))


lblrulez=Label(root,text="This Quizzer contains 5 questions \n This Project was made by Vibhav, Tathagata and Vandana.", justify=CENTER, bg="light blue", fg="red")
lblrulez.pack(pady=(110,0))


root.mainloop()