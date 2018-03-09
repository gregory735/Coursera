#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 16:03:34 2018

@author: gregory
"""
#%%
"""
Problem 2_7:
Heron's formula for computing the area of a triangle with sides a, b, and c is
as follows. Let s = .5(a + b + c) --- that is, 1/2 of the perimeter of the 
triangle. Then the area is the square root of s(s-a)(s-b)(s-c). You can compute
the square root of x by x**.5 (raise x to the 1/2 power). Use an input 
statement to get the length of the sides. Don't forget to convert this input 
to a real number using float(). Adjust your output to be just like what you
see below. Here is a run of my program:

problem2_7()

Enter length of side one: 9

Enter length of side two: 12

Enter length of side three: 15
Area of a triangle with sides 9.0 12.0 15.0 is 54.0
 
"""
#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    s1 = float(input("enter length of side one:"))
    s2 = float(input("enter length of side two:"))
    s3 = float(input("enter length of side three:"))
    area = (s1 + s2 + s3) / 2
    s4 = (area * (area - s1) * (area - s2) * (area - s3)) ** 0.5
    print("Area of a triangle with sides {:.1f} {:.1f} {:.1f} is {:.1f}".format(s1, s2, s3, s4))