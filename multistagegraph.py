INF=0x3f3f3f3f
N=10                 #状态数
K=5                  #阶段数
A=[[0,2,4,3,INF,INF,INF,INF,INF,INF],[INF,0,INF,INF,7,4,INF,INF,INF,INF],
   [INF,INF,0,INF,3,2,4,INF,INF,INF],[INF,INF,INF,0,6,2,5,INF,INF,INF],
   [INF,INF,INF,INF,0,INF,INF,3,4,INF],[INF,INF,INF,INF,INF,0,INF,6,3,INF],
   [INF,INF,INF,INF,INF,INF,0,3,3,INF],[INF,INF,INF,INF,INF,INF,INF,0,INF,3],
   [INF,INF,INF,INF,INF,INF,INF,INF,0,4],[INF,INF,INF,INF,INF,INF,INF,INF,INF,0]]
S=[[0],[1,2,3],[4,5,6],[7,8],[9]]	        #表示5个阶段的状态集合 

def mindist1(start,end):			        #动态规划问题的逆序解法
    dp=[[INF]*N for i in range(K)]
    dp[4][end]=0						    #初始条件
    for k in range(3,-1,-1):			    #从阶段3到阶段0循环 
        for i in range(0,len(S[k])):	    #遍历阶段k中的每个状态 
            xk=S[k][i]				        #阶段k中的状态xk
            for j in range(0,N):
                if A[xk][j]!=0 and A[xk][j]!=INF:   #存在<xk,j>边
                    dp[k][xk]=min(dp[k][xk],A[xk][j]+dp[k+1][j])
    return dp[0][start]

start=0					#起始点 
end=9						#终点 
print("最短路径长度=%d"%(mindist1(start,end)))