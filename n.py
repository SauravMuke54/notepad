from tkinter import * 
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askyesno
from tkinter import filedialog
import webbrowser

root=Tk()
root.title("Notepad")
menu=Menu(root)
root.config(menu=menu)

def openfile():
    f1=filedialog.askopenfilename(title='Open File')
def savefile():
    f1=filedialog.asksaveasfile(title='Open File')
def confirm():
    f1=askyesno()
def newwin():
    new= Toplevel(root)
    new.geometry("750x250")
    new.title("Fonts")
    menu=StringVar()
    Label(new,text="Choose Font").pack(pady=0,padx=0)
    menu.set("Select Font")
    drop=OptionMenu(new,menu,"Calibri","Roman")
    drop.pack(padx=10)
def feed():
    webbrowser.open_new("www.gmail.com")
    
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=openfile)
filemenu.add_command(label='New Window')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='Save As')
filemenu.add_command(label='Exit',command=confirm)

editmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Copy',accelerator="Ctrl+C")
editmenu.add_command(label='Paste',accelerator="Ctrl+V")
editmenu.add_command(label='Undo',accelerator="Ctrl+Z")
editmenu.add_command(label='Redo',accelerator="Ctrl+Y")
editmenu.add_command(label='Delete',accelerator="Delete")


formatmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=formatmenu)
formatmenu.add_checkbutton(label='Word Wrap',command=newwin)
formatmenu.add_command(label='Font',command=newwin)

helpmenu=Menu(menu)
menu.add_cascade(label='Edit',menu=helpmenu)
helpmenu.add_command(label='Help')
helpmenu.add_command(label='Send Feedback',command=feed)
helpmenu.add_command(label='About Notepad')

text=ScrolledText(root,width=200,height=200,undo=True)
text.pack(fill=tk.BOTH)


root.mainloop()



