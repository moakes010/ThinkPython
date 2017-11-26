'''
Exercise 2  
Write a program that creates a Canvas and a Button. When the user presses the Button, it should draw a circle on the canvas.
'''
from swampy.Gui import *

g = Gui()
g.title('Exercise 2')
def cb1():
    item = canvas.circle([0,0], 100, fill='black', outline='white')
    
button = g.bu(text='Draw Circle', command=cb1)
canvas = g.ca(width=500, height=500)
canvas.config(bg='black')

g.mainloop()