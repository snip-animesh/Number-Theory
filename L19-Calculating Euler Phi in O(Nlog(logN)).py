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

while True:
    print(lst[int(input())])
