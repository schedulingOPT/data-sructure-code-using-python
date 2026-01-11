def DFS1(adj,v):       #深度优先遍历
    global visited,ans
    ans.append(v)                         #访问顶点v
    visited[v]=1
    for u in adj[v]:                 #找到v的相邻点u
        if visited[u]==0:               #若顶点u尚未访问
          DFS1(adj,u)                 #从u出发继续搜索
def DFS(adj,v):
    global visited,ans
    ans=[]      #存放一个DFS序列
    visited=[0]*len(adj)           #初始化所有元素为0
    DFS1(adj,v)
    return ans

adj=[[1,3],[0],[3,4],[0,2,4],[2,3]]
n=len(adj)
print("G: ")
for i in range(0,n):
    print("  ",i,end=': ')
    print(adj[i])
v=0
ans=DFS(adj,0)
print("DFS(%d): "%(v),ans)
