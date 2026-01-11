INF=0x3f3f3f3f
N=10                 #状态数
K=5                  #阶段数
A=[[0,2,4,3,INF,INF,INF,INF,INF,INF],[INF,0,INF,INF,7,4,INF,INF,INF,INF],
   [INF,INF,0,INF,3,2,4,INF,INF,INF],[INF,INF,INF,0,6,2,5,INF,INF,INF],
   [INF,INF,INF,INF,0,INF,INF,3,4,INF],[INF,INF,INF,INF,INF,0,INF,6,3,INF],
   [INF,INF,INF,INF,INF,INF,0,3,3,INF],[INF,INF,INF,INF,INF,INF,INF,0,INF,3],
   [INF,INF,INF,INF,INF,INF,INF,INF,0,4],[INF,INF,INF,INF,INF,INF,INF,INF,INF,0]]
S=[[0],[1,2,3],[4,5,6],[7,8],[9]]	        #表示5个阶段的状态集合 

def mindist2(start,end):			        #动态规划问题的逆序解法
    dp=[[INF]*N for i in range(K)]
    dp[0][start]=0						    #初始条件
    for k in range(1,K):			    #从阶段1到阶段K-1循环 
        for i in range(0,len(S[k])):	    #遍历阶段k中的每个状态 
            xk=S[k][i]				        #阶段k中的状态xk
            for j in range(0,N):
                if A[j][xk]!=0 and A[j][xk]!=INF:   #存在<j,xk>边
                    dp[k][xk]=min(dp[k][xk],dp[k-1][j]+A[j][xk])
    return dp[4][end]

start=0					    #起始点 
end=9						#终点 
print("最短路径长度=%d"%(mindist2(start,end)))