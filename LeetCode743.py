class Solution:
    INF=0x3f3f3f3f
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for i in range(n)]              	#图的邻接表
        for x in times:                				#遍历times建立邻接表
            adj[x[0]-1].append([x[1]-1,x[2]])
        dist=self.Dijkstra(adj,n,k-1)
        ans=dist[0]
        for i in range(1,n):
            ans=max(ans,dist[i])
       	if ans==self.INF:return -1
       	else:return ans

    def Dijkstra(self,adj,n,v):        	#Dijkstra算法
        dist=[self.INF]*n
        S=[False]*n
        minpq=[]                        #定义一个小根堆
        dist[v]=0
        heapq.heappush(minpq,[dist[v],v])
        while minpq:
            x=heapq.heappop(minpq)      #出队结点e
            u=x[1]
            S[u]=True
            for e in adj[u]:
                v,w=e[0],e[1]
                if not S[v] and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    heapq.heappush(minpq,[dist[v],v])
        return dist
