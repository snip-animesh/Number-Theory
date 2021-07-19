def phi(n):
    res,i=n,2
    while(i*i<=n):
        if n%i==0:
            res//=i
            res*=(i-1)
            while(n%i==0):
                n//=i
        i+=1

    # If n has a prime factor greater than sqrt(n)
    # (There can be at-most one  such prime factor)
    if n>1:
        res//=n
        res*=(n-1)
    return res
    
    
