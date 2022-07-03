def rev(n):
    p=0
    while(n):
        r=n%10
        n=n//10
        p=p*10+r
    return p
n=int(input())    
arr=list(map(int,input().strip().split()))
t=[]
for i  in range(n):
    t.append(rev(arr[i]))
for i in range(n):
    print(t[i],end=" ")