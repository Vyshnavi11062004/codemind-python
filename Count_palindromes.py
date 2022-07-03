n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    p=str(a[i])
    k=p[::-1]
    if p==str(k):
        c=c+1
print(c)        