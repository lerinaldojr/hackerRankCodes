#!/bin/python
import sys
N = int(raw_input().strip())
if(N%2 == 0):
    if(N>=2 and N<=5) or (N>20):
        print('Not Weird')
    elif(N>=6 and N<=20):
        print('Weird')
else:
    print('Weird')