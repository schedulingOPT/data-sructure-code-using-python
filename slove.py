def Solve(a,m,n,s):
    if m!=n:return False
    s[0]=0
    for i in range(0,n):s[0]+=a[i][i]
    return True

a=[[1,2,3],[4,5,6],[7,8,9]]
m=len(a)
n=len(a[0])
s=[0]
Solve(a,m,n,s)
print(s[0])

    
    