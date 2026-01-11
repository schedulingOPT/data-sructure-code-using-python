class Solution:
    def networkDelayTime(self,times: List[List[int]],n: int,k:int)->int:
        INF=0x3f3f3f3f
        adj=[[] for i in range(n)]     			#图的邻接表
        for x in times:                						#遍历times建立邻接表
            adj[x[0]-1].append([x[1]-1,x[2]])
        dist=[INF]*n        						 #dist[i]:源点到i的最短路径长度
        s=k-1                          							#源点为s
        dist[s]=0
        qu=deque()   	#定义一个队列qu
        qu.append(s)                								#源点结点进队
        while qu:              					#队列不空循环
            u=qu.popleft()                						#出队顶点u
            for e in adj[u]:
                v,w=e[0],e[1]             						#相邻顶点为v
                if dist[u]+w<dist[v]: 						#边松驰:u到v有边且路径长度更短
                    dist[v]=dist[u]+w
                    qu.append(v)               		 				#顶点v进队
        ans=dist[0]
        for i in range(1,n):
            ans=max(ans,dist[i])
        if ans==INF:return -1
        else: return ans


class Solution:
    def networkDelayTime(self,times: List[List[int]],n: int,k:int)->int:
        INF=0x3f3f3f3f
        adj=[[] for i in range(n)]     			#图的邻接表
        for x in times:                						#遍历times建立邻接表
            adj[x[0]-1].append([x[1]-1,x[2]])
        dist=[INF]*n        						 #dist[i]:源点到i的最短路径长度
        visited=[False]*n
        s=k-1                          							#源点为s
        dist[s]=0
        qu=deque()   	#定义一个队列qu
        qu.append(s)                								#源点结点进队
        visited[s]=True
        while qu:             					#队列不空循环
            u=qu.popleft()          						#出队顶点u
            visited[u]=False
            for e in adj[u]:
                v,w=e[0],e[1]                                   #相邻顶点为v
                if dist[u]+w<dist[v]: 						#剪支：u到v有边且路径长度更短
                    dist[v]=dist[u]+w
                    if not visited[v]:         					#若顶点v不在队中
                        qu.append(v)            					#将顶点v进队
                        visited[v]=True
        ans=dist[0]
        for i in range(1,n):
            ans=max(ans,dist[i])
        if ans==INF:return -1
        else: return ans
