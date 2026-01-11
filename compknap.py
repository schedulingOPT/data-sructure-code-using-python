def dfs(cw,cv,i):    #回溯算法
    global w,v,n,W,bestv
    if i>=n:
        print("一个解,cw=%d,cv=%d"%(cw,cv))
        if cw<=W and cv>bestv:           #找到一个更优解
            bestv=cv
    else:
        print("不选择物品i=%d,dfs(%d,%d,%d)"%(i,cw,cv,i+1))
        dfs(cw,cv,i+1)                 #不选择物品i      
        if cw+w[i]<=W:
            print("选择物品i=%d,再选i一件,dfs(%d,%d,%d)"%(i,cw+w[i],cv+v[i],i))        
            dfs(cw+w[i],cv+v[i],i)       #剪支:选择物品i,然后继续选择物品i
        else:
            print("选择物品i=%d,再选i一件,dfs(%d,%d,%d)->cut"%(i,cw+w[i],cv+v[i],i))        
        if cw+w[i]<=W:
            print("选择物品i=%d,再选下一件,dfs(%d,%d,%d)"%(i,cw+w[i],cv+v[i],i+1))
            dfs(cw+w[i],cv+v[i],i+1)     #剪支:选择物品i,然后选下一件 
        else:
            print("选择物品i=%d,再选下一件,dfs(%d,%d,%d) ->cut"%(i,cw+w[i],cv+v[i],i+1))

def compknap(w,v,n,W):
    global bestv
    bestv=0                 #存放最大价值,初始为0
    dfs(0,0,0)
    print("最大价值=",bestv)

n=2; 
w=[1,2]
v=[2,5]
W=2
compknap(w,v,n,W)