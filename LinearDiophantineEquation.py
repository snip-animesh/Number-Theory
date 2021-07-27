def extendedEuclid(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=extendedEuclid(b,a%b)
    x=y1
    y=(x1-(a//b)*y1)
    return g,x,y


def lde(a,b,c):
    g,x0,y0=extendedEuclid(abs(a),abs(b))
    if (c%g):
        return "Solution doesn't exist"
    x=x0*(c//g)
    y=y0*(c//g)
    if a<0:
        x=-x
    if b<0:
        y=-y
    return x,y
