
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

def seconds_to_time(s):
    '''
    return time object with hours:mintues:seconds
    '''
    t = Time()
    m, t.seconds = divmod(s, 60)
    t.hour, t.minutes = divmod(m, 60)
    return t

def print_time(time_obj):
    '''
    Take time object and pring in format

    hour:minute:second
    '''
    print("%.2d:%.2d:%.2d" % (time_obj.hour, time_obj.minutes, time_obj.seconds))

def increment(time, seconds):
    '''
    create and return new time object
    '''
    return seconds_to_time(time_to_seconds(time) + seconds)

t1 = Time()
t1.hour = 23
t1.minutes = 59
t1.seconds = 50

delta = 10

print_time(increment(t1, delta))

