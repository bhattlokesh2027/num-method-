def f(x):
    x1=0
    y1=1
    x2=1
    y2=2
    x3=2
    y3=4
    a=((x-x2)*(x-x3))/((x1-x2)*(x1-x3))*y1
    b=((x-x1)*(x-x3))/((x2-x1)*(x2-x3))*y2
    c=((x-x1)*(x-x2))/((x3-x1)*(x3-x2))*y3
    fx=a+b+c
    return(fx)
def of(x):
   return(2**x)
l=f(1.5)
o=of(1.5)
print("exact value is",o)
print("interpolated value is",l)
