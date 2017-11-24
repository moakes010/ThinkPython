'''
Exercise 3  
Write a str method for the Point class. Create a Point object and print it.
'''

class Point(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point (x,y) at (%.2d,%.2d)" % (self.x, self.y)

p = Point(10, 11)
print(p)