import numpy as np
def f(x):
   return(10-(x*x))
c=f(-2)+f(2)
a=-2
b=2
n=int(input("enter the intervals"))
h=(b-a)/n
s=0
for i in range(1,n):
    d=a+i*h
    e=f(d)
    s=s+e
area=((c/2)+s)*h
print("the area is ",area)
