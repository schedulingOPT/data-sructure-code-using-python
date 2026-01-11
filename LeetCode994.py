class QNode:                        			#队列结点类
    def __init__(self,x,y):						#构造函数
        self.x,self.y=x,y             			#当前位置(x,y)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx=[0,0,1,-1]                        #水平方向偏移量
        dy=[1,-1,0,0]                        #垂直方向偏移量
        m,n=len(grid),len(grid[0])                	#行列数
        qu=deque()      	#定义一个队列qu
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]==2:qu.append(QNode(i,j))  #所有腐烂的橘子进队
        ans=0                                        		#经过的最小分钟数
        while qu:                                  	#队不空循环
            flag=False
            cnt=len(qu)                       		#求队列中元素个数cnt
            for i in range(0,cnt):                 		#循环cnt次处理该层所有结点
                e=qu.popleft()              					#出队结点e
                for di in range(0,4):                     	#四周搜索
                    nx,ny=e.x+dx[di],e.y+dy[di]
                    if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==1:
                       	grid[nx][ny]=2             		#新鲜橘子变为腐烂橘子
                        qu.append(QNode(nx,ny))       	#腐烂橘子进队
                        flag=True        #表示有新鲜橘子变为腐烂橘子
            if flag: ans+=1			#有新鲜橘子变为腐烂橘子时ans增1
        for i in range(0,m):                       		#判断是否还存在新鲜橘子
            for j in range(0,n):
                if grid[i][j]==1:return -1    		#还存在新鲜橘子
       	return ans
