t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    total=n*(n+1)//2
    for j in range(n-1):
        s+=l[j]
    print(total-s)