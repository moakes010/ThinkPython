

from swampy.Gui import *

colors=['white', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
cir=None
g = Gui()
g.title('Exercise 3')
def cb1():
    cir = canvas.circle([0,0], 100, fill='black', outline='white')
    global cir
def cb2():
    if cir == None:
        return
    color = entry.get()
    if color in colors:
        cir.config(outline=color)
    else:
        raise ValueError
    

button = g.bu(text='Draw Circle', command=cb1)
entry = g.en(text='white')
button_change_color = g.bu(text='Change', command=cb2)
canvas = g.ca(width=500, height=500)
canvas.config(bg='black')

g.mainloop()