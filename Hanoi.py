def Hanoi(n,x,y,z):
    if n==1:
        print("将盘片%d从%c搬到%c"%(n,x,z))
    else:
        Hanoi(n-1,x,z,y)
        print("将盘片%d从%c搬到%c"%(n,x,z))
        Hanoi(n-1,y,x,z)

n=3
x='X'
y='Y'
z='Z'
Hanoi(n,x,y,z)
