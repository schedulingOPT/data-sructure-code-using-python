class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m,n=2,3
        t="123450"
        s=""
        for i in range(0,m):   			#将board转换为一个字符串
            for j in range(0,n):
                s+=str(board[i][j])
        adj=[[1,3],[0,4,2],[1,5],[0,4],[1,3,5],[2,4]]
        qu=deque()        	        #定义一个队列
        visited=set()   	        #状态访问标记
        qu.append(s)                #初始状态s进队
        visited.add(s)
        ans=0                       #最少移动次数
        while qu:
            cnt=len(qu)                 #队不空时循环
            for k in range(0,cnt):
                curs=qu.popleft()              #出队curs
                if curs==t:return ans           #找到目标状态时返回ans
                i=curs.index('0')               #查找'0'的位置i
                for j in adj[i]:                #找到位置i的相邻位置j
                    nboard=self.swap(curs,i,j)  #扩展
                    if nboard not in visited:   #nboard状态没有访问过
                        qu.append(nboard)       #nboard状态进队
                        visited.add(nboard)     #置已访问标记
            ans+=1
        return -1

    def swap(self,s,i,j):    			#返回s[i]与s[j]交换的结果
        a=list(s)                       #将s转换为列表a
        a[i],a[j]=a[j],a[i]             #a[i]和a[j]交换
        return ''.join(a)               #连接为新字符串后返回
