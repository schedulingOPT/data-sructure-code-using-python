class QNode:                        #队列结点类
    def __init__(self,x,y):
        self.p=x					#当前位置
        self.bstep=y				#从当前位置向后跳次数

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        MAXX=6000
        visited=[[False]*2 for i in range(0,MAXX+1)]
        for e in forbidden:
            visited[e][0]=visited[e][1]=True	#forbidden中所有位置为不可访问的
        qu=deque()     			#定义一个队列qu
        qu.append(QNode(0,0))               						#起始点进队
        visited[0][0]=True								#置已访问标记
        ans=0          									#最少跳跃次数
        while qu:
            cnt=len(qu)								#求队列中元素个数为cnt
            for i in range(0,cnt):
                e=qu.popleft()        							#出队结点e
                curx,bstep=e.p,e.bstep
                if curx==x:return ans								#遇到x返回ans
                e1=QNode(curx+a,0)      #向前跳跃一次，建立队列结点e1
                if e1.p<=MAXX and not visited[e1.p][e1.bstep]:
                    visited[e1.p][e1.bstep]=True						#置已访问标记
                    qu.append(e1)											#结点e1进队
               	e2=QNode(curx-b,bstep+1)				#向后跳跃一次，建立队列结点e2
                if e2.p>=0 and e2.bstep<2 and not visited[e2.p][e2.bstep]:
                    visited[e2.p][e2.bstep]=True		#置已访问标记
                    qu.append(e2)						#结点e2进队
            ans+=1										#跳跃次数增1
        return -1										#不能跳到x返回-1