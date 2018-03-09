#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 15:20:28 2018

@author: gregory
"""

#%%
"""Problem 2_1:
Write a function 'problem2_1()' that sets a variable lis = list(range(20,30)) and
does all of the following, each on a separate line: 
(a) print the element of lis with the index 3
(b) print lis itself
(c) write a 'for' loop that prints out every element of lis. Recall that 
    len() will give you the length of such a data collection if you need that.
    Use end=" " to put one space between the elements of the list lis.  Allow
    the extra space at the end of the list to stand, don't make a special case
    of it.
"""  
#%%      
def problem2_1():
    lis = list(range(20,30))
    print(lis[3])
    print(lis[0:])
    for i in range(20,30):
        print(i, end=' ')