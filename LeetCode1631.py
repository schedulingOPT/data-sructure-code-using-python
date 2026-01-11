class QNode:					            #优先队列结点类
    def __init__(self,x,y,length):          #构造方法
        self.x,self.y=x,y	      			#位置
        self.length=length		  			#路径长度
    def __lt__(self,other):	    		    ##按length越小越优先出队
        return self.length<other.length

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF=0x3f3f3f3f
        dx=[0,0,1,-1]                            				#水平方向偏移量
        dy=[1,-1,0,0]                       	 				#垂直方向偏移量
        m,n=len(heights),len(heights[0])
        dist=[[INF]*n for i in range(m)]           #dist[m][n]
        pqu=[]                    #定义一个优先队列pqu
        heapq.heappush(pqu,QNode(0,0,0))			#源点结点进队
        dist[0][0]=0
        while pqu:				#队列不空循环
            e=heapq.heappop(pqu)	        #出队结点e
            x,y=e.x,e.y
            if x==m-1 and y==n-1: return e.length   		#找到终点返回
            for di in range(0,4):
                nx,ny=x+dx[di],y+dy[di]
                if nx<0 or nx>=m or ny<0 or ny>=n:continue
                curlen=max(e.length,abs(heights[nx][ny]-heights[x][y]))
                if curlen<dist[nx][ny]:      			#剪支：当前路径长度更短
                    dist[nx][ny]=curlen
                    e1=QNode(nx,ny,curlen)              #创建子结点e1
                    heapq.heappush(pqu,e1)				#结点e1进队                     
        return -1
