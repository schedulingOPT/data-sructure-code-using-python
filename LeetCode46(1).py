def dfs(x,i):		#回溯算法
    if i==len(x):
        print(x)
    else:
        for j in range(i,len(x)):
            x[i],x[j]=x[j],x[i]     #x[i]后x[j]交换
            dfs(x,i+1)
            x[i],x[j]=x[j],x[i]     #回溯

def perm(a):            #求a的全排列
    x=a                 #解向量
    dfs(x,0)

a=[1,2,3]
perm(a)