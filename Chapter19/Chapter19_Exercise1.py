

from swampy.Gui import *

g = Gui()
g.title('Exercise 1')
def cb1():
    g.bu(text="Second Button", command=cb2)
def cb2():
    g.la(text="Nice Job")
button = g.bu(text='First Button', command=cb1)
g.mainloop()