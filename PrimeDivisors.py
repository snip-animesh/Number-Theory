def primedivs(a):
    i,divs=2,set()
    n=a
    while(i*i<=n):
        if not a%i:
            divs.add(i)
            while (a%i==0):
                a//=i
        i+=1
    if a>2:
        divs.add(a)
    return divs
  
  #Return a set of prime divisors of a
