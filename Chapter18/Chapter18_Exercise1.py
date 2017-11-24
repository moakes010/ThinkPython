'''
Exercise 1  
Write a __cmp__ method for Time objects. Hint: you can use tuple comparison, but you also might consider using integer subtraction.
'''

#Note: cmp no longer exists in python3. Should use __lt__ instead.

class Time(object):
    '''
    Represents time of day

    attributes: hour, minute, second
    '''
    def time_to_seconds(self, t):
        '''
        return total seconds of time obj
        '''
        return (t.hour * 60 + t.minutes)*60 + t.seconds


    def __cmp__(self, other):
        '''
        Takes two params, self and other. Both time objects

        Returns codes: 

        return 1 if the first object is greater
        return -1 if the second object is greater
        return 0 if if the objects are equal
        '''
        t1 = self.time_to_seconds(self)
        t2 = self.time_to_seconds(other)
        return cmp(t1, t2)

t1 = Time()
t1.hour = 10
t1.minutes = 30
t1.seconds = 30
t2 = Time()
t2.hour = 11
t2.minutes = 30
t2.seconds = 30

print(cmp(t1, t2))



        

