import numpy as np

def fx(x):
    return(x*x-10)
def fdx(x):
    return(2*x)
a=float(input("input any no."))
b=int(input("enter interations"))
c=1
while(c<=b):
    r=a-fx(a)/fdx(a)
    c=c+1
    a=r

print("the root is",a)
