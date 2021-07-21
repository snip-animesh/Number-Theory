lst=list(range(0,1000001))
i=2
while(i<1000001):
    if lst[i]==i:
        j=i
        while(j<1000001):
            lst[j]//=i
            lst[j]*=(i-1)
            j+=i
    i+=1


def getCount(d,n):
    return lst[n//d]


n=int(input())
res,i=1,2
while(i*i<=n):
    if (n%i==0):
        d1=i
        d2=n//i
        res+=d1*getCount(d1,n)
        if d1!=d2:
            res+=d2*getCount(d2,n)
    i+=1
print(res+n)

#Overall complexity O((log(logN))+sqrt(N))
