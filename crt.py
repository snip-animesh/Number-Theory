#Chinese Reaminder Theorem .. 

from functools import reduce


def extendedEuclid(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=extendedEuclid(b,a%b)
    x=y1
    y=(x1-(a//b)*y1)
    return g,x,y


def crt (nums, reminders):
    zipper=dict(zip(nums,reminders))
    Ans=0
    for num,rems in zipper.items():
        g,x,y=extendedEuclid(P//num,num)
        inv=x+num
        Ans+=rems*(P//num)*inv
    return Ans


nums=[int(x) for x in input().split()]
remainders=[int(x) for x in input().split()]
P = reduce((lambda x,y: x*y),nums)
Ans=crt(nums,remainders)
print(Ans%P)
