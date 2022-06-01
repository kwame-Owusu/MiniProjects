
from tkinter import *
from tkinter.ttk import *
from time import strftime

root= Tk()
root.title("Hello")


#lable widget
word = Label(root,text="Hello World!",font=("FiraMono-Regular", 80), background="white", foreground="cyan" )
word.pack(anchor="center")


    


#pop up and  wait for user interface
mainloop()
