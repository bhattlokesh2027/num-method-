def f(x):
    return(10-(3*x*x))
a=-1
b=3
n=4
h=(b-a)/n
d=f(a)+f(b)
s=0
p=0
for i in range(1,4):
    x=a+(i*h)
    if (i%2==0):
        s=s+(2*f(x))
    else:
        p=p+(4*f(x))
e=s+p
l=(h*(d+e))/3
print("the integration is",l)

