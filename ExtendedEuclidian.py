def extendedEuclid(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=extendedEuclid(b,a%b)
    x=y1
    y=(x1-(a//b)*y1)
    return g,x,y


a,b=map(int,input().split()) 
# a>b
g,x,y=extendedEuclid(a,b)
print(f'{a}*{x}+{b}*{y}={g}')
