def primefactors(n):
    pfactors=[]
    if n==1:
        pfactors=[(1,1)]
    else:
        i=2
        while(i*i<=n):
            count=0
            if n%i==0:
                while(n%i==0):
                    n//=i
                    count+=1
                pfactors.append((i,count))
            i+=1
        if n>=2:
            pfactors.append((n,1))
    return pfactors
