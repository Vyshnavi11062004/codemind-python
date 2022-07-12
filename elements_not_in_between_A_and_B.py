n=int(input())
a=list(map(int,input().split()))
b,c=map(int,input().split())
s=[]
p=[]
for i in range(b,c+1):
    s.append(i)
for j in a:
    if j not in s:
        p.append(j)
if len(p)>0:
    print(*p)
else:
    print('-1')