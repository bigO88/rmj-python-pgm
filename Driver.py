'''
Created on Nov 11, 2017

@author: rajjanwa
'''

import base.Calculator as calc
from __builtin__ import raw_input

def applyCal(x,y,z):
    print("The result is as:")
    if z== 1:
        print(calc.add(x, y))
    elif z == 2:
        print(calc.sub(x, y))
    elif z==3 :
        print(calc.divide(x, y))
    elif z==4 :
        print(calc.multi(x, y))        
         
            
   
        
if __name__ == '__main__':
    x=raw_input("Enter First number")
    y=raw_input("Enter second number")
    z=raw_input("Enter operation")
    
    applyCal(int(x),int(y),int(z))