import os, sys
from swampy.Gui import *
from PIL import Image, ImageTk

class ImageBrowser(Gui):
    def __init__(self):
        Gui.__init__(self)

        # clicking on the image breaks out of mainloop
        self.button = self.bu(command=self.quit, relief='flat')

    def image_loop(self, dirname='.'):
        files = os.listdir(dirname)
        for file in files:
            try:
                self.show_image(file)
                print file
                self.mainloop()
            except IOError:
                continue
            except:
                break

    def show_image(self, filename):
        image = Image.open(filename)
        self.tkpi = ImageTk.PhotoImage(image)
        self.button.config(image=self.tkpi)

def main(script, dirname='.'):
    g = ImageBrowser()
    g.image_loop(dirname)

if __name__ == '__main__':
    main(*sys.argv)