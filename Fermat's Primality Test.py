import random
def fermatPrime(p):
    if p==1 or p==4:
        return False
    elif p==2 or p==3:
        return True
    else:
        for i in range(5):
            a=random.randint(2, p - 2)
            if pow(a,p-1,p)!=1:
                return False
        return True


for _ in range(int(input())):
    print("YES") if fermatPrime(int(input())) else print("NO")
