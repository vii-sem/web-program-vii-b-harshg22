#You can't install tkinter using pip because tkinter is an interface to a C++ library called Tk, whereas pip is coded with Python.

#Luckily you do not have to worry about the above statement because tkinter comes as a built-in library for the standard Python distribution.

#So what you have to do is:

#Go to your virtualenv directory: cd to_your_virtualenv_directory
#Activate it: source bin/activate
#Access your python shell within it: python
#Then import tkinter as tk
#now 

from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app") 
window.geometry('350x200')
rad1 = Radiobutton(window,text='First', value=1) 
rad2 = Radiobutton(window,text='Second', value=2) 
rad3 = Radiobutton(window,text='Third', value=3) 
rad1.grid(column=0, row=0)
rad2.grid(column=1, row=0)
    
rad3.grid(column=2, row=0) 
window.mainloop()
