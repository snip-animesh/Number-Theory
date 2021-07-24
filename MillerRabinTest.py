import random

def miller(d,n):
    a=random.randint(2,n-2)
    x=pow(a,d,n)
    if x==1 or x==n-1:
        return True
    while d!=n-1:
        x=(x*x)%n
        d=d*2
        if x==n-1:
            return True
        elif x==1:
            return False
    return False


def isPrime(n):
    if n==2 or n==3:
        return True
    elif n<5:
        return False
    d=n-1
    while(d%2==0):
        d//=2
    for i in range(5):
        if not miller(d, n):
            return False
    return True


for _ in range(int(input())):
    print("YES") if isPrime(int(input())) else print("NO")
