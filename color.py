def judge(i,j):					#判断顶点i是否可以着上颜色j
    global A,n,m,x,ans
    for k in range(0,len(A[i])):
        if x[A[i][k]]==j:return False	#存在相同颜色的顶点
    return True

def dfs(i):					#递归回溯算法
    global m,x,ans
    if i>=n:ans+=1												#达到一个叶子结点
    else:
        for j in range(0,m):
            x[i]=j						#置顶点i为颜色j
            if judge(i,j):dfs(i+1)		#若顶点i可以着上颜色j
            x[i]=-1 									#回溯

def colors(A,n,m):		#求图的m着色问题
    global x,ans
    x=[-1]*n        #解向量元素初始化为-1
    ans=0
    dfs(0)			        #从顶点0开始搜索
    return ans

n,m=4,3
A=[[1,2,3],[0],[0,3],[0,2]]
print("共有%d种着色方案"%(colors(A,n,m)))