#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:00:40 2018

@author: Grégory
"""
#%%
"""
Problem 1_4:
Write a function 'problem1_4(miles)' to convert miles to feet. There are
5280 feet in each mile. Make the print out a statement as follows:
"There are 10560 feet in 2 miles."  Except for the numbers this statement 
should be exactly as written.

Tip: Watch the spacing before and after your numbers.  Make sure that it is 
just one space or the auto-grader may not give you credit.
"""
#%%
def problem1_4(miles):
    feet = 5280
    result = feet * miles
    print('There are {} feet in {} miles.'.format(result,miles))