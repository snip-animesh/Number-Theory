-----Using Recursion------


def binaryExpo(base,power,res=1):
    if power==0:
        return 1

    elif power==1:
        return base*res
    elif power%2==0:
        return binaryExpo(base*base,power//2,res)
    else:
        return binaryExpo(base,power-1,res*base)
      
      
 ---------- Using Loop -------

def binaryExpo(base,power):
    res=1
    while(power>0):
        if power%2==0:
            base*=base
            power//=2
        else:
            res*=base
            power-=1
    return res
