import tkinter as tk 
from tkinter import ttk

def get_screen_size(window):
    return window.winfo_screenwidth(),window.winfo_screenheight()
 
def get_window_size(window):
    return window.winfo_reqwidth(),window.winfo_reqheight()
 
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)
    print(size)
    root.geometry(size)


window = tk.Tk()

window.title = "wode window"
center_window(window,300,300)
window.attributes("-topmost",True) #窗口在最上层
ttk.Style().configure('ZC.TButton', foreground='pink',relief="flat", background='white')
ttk.Style().configure('ZC.TLabel', foreground='green', background='pink')

l = ttk.Label(text='nihao',style='ZC.TLabel')
l.pack()

def goto():
    print('sssss')

b = ttk.Button(text = "anniu",style='ZC.TButton',command = goto)
b.pack()

window.mainloop()