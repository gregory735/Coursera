#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:00:40 2018

@author: Grégory
"""
#%%
"""
Problem 1_3:  
Write a function problem1_3(n) that adds up the numbers 1 through n and
prints out the result. You should use either a 'while' loop or a 'for' loop.
Be sure that you check your answer on several numbers n.  Be careful that your
loop steps through all the numbers from 1 through and including n.

Tip: As this involves a loop you could make an error that causes it to run 
forever. Usually Control-C will stop it. See suggestions at the beginning of 
this document.  With loops take care that your first and last iterations are
what you expect. A print statement can be inserted in the loop to monitor it, 
but be sure this isn't in the submitted function.
"""
#%%
def problem1_3(n):
    my_sum = 0
    for i in range (1, n + 1):
        my_sum += i
    print(my_sum)