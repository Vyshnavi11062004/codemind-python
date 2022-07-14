n=input()
s=''
for i in n:
    if i not in s:
        s=s+i
if len(n)==len(s):
    print('True')
else:
    print('False')