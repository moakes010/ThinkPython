'''
Exercise 4  
Write an add method for the Point class
'''

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point (x,y) at (%.2d,%.2d)" % (self.x, self.y)
    
    def __add__(self, p):
        return (self.x + p.x, self.y + p.y)

p = Point(1,2)
p2 = Point(2,3)

print(p + p2)