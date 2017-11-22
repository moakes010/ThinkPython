'''
Chapter 10 Exercise 3  
Write a function that takes a list of numbers and returns the cumulative sum; that is, 
a new list where the ith element is the sum of the first i+1 elements from the original list. 
For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
'''

test=[2,2,5]
def cumulative_sum(my_list):
    cs_list = [ sum(test[0:i+1]) for i in range(len(my_list)) ]
    return cs_list
        
print(cumulative_sum(test))
        