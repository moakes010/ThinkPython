'''
Exercise 1  
Write a function called print_time that takes a Time object and prints it in the form hour:minute:second. 
Hint: the format sequence '%.2d' prints an integer using at least two digits, including a leading zero if necessary.
'''

class Time(object):
    '''
    Represents time of day

    attributes: hour, minute, second
    '''

def print_time(time_obj):
    '''
    Take time object and pring in format

    hour:minute:second
    '''
    print("%.2d:%.2d:%.2d" % (time_obj.hour, time_obj.minutes, time_obj.second))

time = Time()
time.hour = 8
time.minutes = 31
time.second = 40

print_time(time)


