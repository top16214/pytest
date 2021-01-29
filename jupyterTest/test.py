#!/usr/bin/env

'''You will get to see a new type of operator which is being known as the walrus operator (:=). This allows you to assign variables inside an expression. The major benefit of this is to save you some lines of code and you can write even cleaner and compact code in Python.'''

num = [1,2,3,4,5]
if( (size:=len(num)) < 10 ):
    print(f"Length of list is small, size={size}")
print("size=%d" % size)
