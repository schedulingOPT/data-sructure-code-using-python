import copy
def dfs11(adj,u,v,x):  #深度优先搜索
    global visited,ans
    x.append(u)                           #访问顶点u
    visited[u]=1
    if u==v:                          #找到一条路径
        ans.append(copy.deepcopy(x))     #将路径x的拷贝添加到ans中
        visited[u]=0                    #置u可以重新访问
        x.pop()          #路径回退
        return
    for w in adj[u]:                #找到u的相邻点w
        if visited[w]==0:               #若顶点w尚未访问
            dfs11(adj,w,v,x)             #从w出发继续搜索
    visited[u]=0                       #u出发的所有路径找完后回退
    x.pop()             #路径回退

def dfs1(adj,u,v):   #求u到v的所有路径
    global visited,ans
    ans=[]
    visited=[0]*len(adj)           #初始化所有元素为0
    x=[]
    dfs11(adj,u,v,x)
    return ans

def dfs21(adj,u,v,x):    #回溯法
    global visited,ans
    if u==v:                           #找到一条路径
        ans.append(copy.deepcopy(x))     #将路径x的拷贝添加到ans中
    else:
        for w in adj[u]:               #找到u的相邻点w
            if visited[w]==0:             #若顶点w尚未访问
                x.append(w)                   #访问v,将v添加到ans中
                visited[w]=1
                dfs21(adj,w,v,x)                 #从w出发继续搜索
                visited[w]=0;                   #从w回退到u
                x.pop()
                
def dfs2(adj,u,v):                      #求u到v的所有路径
    global visited,ans
    ans=[]                          #存放所有路径
    visited=[0]*len(adj)           #初始化所有元素为0
    x=[]
    x.append(u)                    #起始点u添加中x中    
    visited[u]=1
    dfs21(adj,u,v,x)
    return ans


adj=[[1,3],[0],[3,4],[0,2,4],[2,3]]
n=len(adj)
print("G: ")
for i in range(0,n):
    print("  ",i,end=': ')
    print(adj[i])

u,v=0,4
print("求%d->%d"%(u,v),"所有路径:")
print("  DFS:    ",end='')    
ans1=dfs1(adj,u,v)
for y in ans1:print(y,end=' ')
print()
print("  回溯法: ",end='')
ans2=dfs2(adj,u,v)
for y in ans2:print(y,end=' ')
print()

