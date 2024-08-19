from tkinter import ttk 
from tkinter import *

def ChangeText():
    label.config(text="Hi this a test for tkinter")
def ChangeText2():
    label2.config(text="label 2 changes")
    
def change_text():
    username = name.get()
    label.config(text=f'Hi {username}')

root = Tk()

root.title("Hello World App")

label = ttk.Label(text="Data Binaries")
label.pack()

label2 = ttk.Label(text="label 2")
label2.pack()

name = ttk.Entry(root)
name.pack()

button = ttk.Button(text='Me' , command=change_text)
button.pack()
button = ttk.Button(text='Clik Me' , command=ChangeText)
button.pack()
button = ttk.Button(text='Quit' , command=root.destroy)
button.pack()
root.mainloop()