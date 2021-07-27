from collections import Counter
n=1000001
arr=[1]*n
for i in range(2,n):
    if arr[i]==1:
        arr[i]=i
        for j in range(i*i,n,i):
            arr[j]=i

n,lst=int(input()),[]
while(n>1):
    lst.append(arr[n])
    n//=arr[n]
if n>=2:
    lst.append(n)
print(Counter(lst))
