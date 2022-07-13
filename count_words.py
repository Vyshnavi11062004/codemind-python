a=str(input())
b=a.lower()
c=b.split()
count=0
for i in range(len(c)):
    m=0
    s=0
    d=list(c[i])
    if d[0]=='a' or d[0]=='e' or d[0]=='i' or d[0]=='o' or d[0]=='u':
        m=m+1
    if d[len(d)-1]!='a' and d[len(d)-1]!='e' and d[len(d)-1]!='i' and d[len(d)-1]!='o' and d[len(d)-1]!='u':
        s=s+1
    if m+s==2:
        count=count+1
print(count)