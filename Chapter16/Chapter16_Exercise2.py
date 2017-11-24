

class Time(object):
    '''
    Represents time of day

    attributes: hour, minute, second
    '''
def time_to_seconds(t):
    '''
    return total seconds of time obj
    '''
    return (t.hour * 60 + t.minutes)*60 + t.seconds

def is_after(t1, t2):
    '''
    Take two time objects

    return true if t1 follows t2 chronologically
    return false if otherwise
    '''
    return time_to_seconds(t1) > time_to_seconds(t2) 

t1 = Time()
t1.hour = 12
t1.minutes = 31
t1.seconds = 45

t2 = Time()
t2.hour = 11
t2.minutes = 32
t2.seconds = 40

print(is_after(t1, t2))
