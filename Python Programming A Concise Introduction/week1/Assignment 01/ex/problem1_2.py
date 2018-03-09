#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 18:00:40 2018

@author: Grégory
"""
#%%
"""
Problem 1_2:
Write a function problem1_2(x,y) that prints the sum and product of the
numbers x and y on separate lines, the sum printing first.
"""
#%%
def problem1_2(x,y):
    soma = x + y
    product = x * y
    print('{}\n{}'.format(soma,product))