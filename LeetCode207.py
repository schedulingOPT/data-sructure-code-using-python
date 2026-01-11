class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses;                                #入度数组
        adj=[[] for i in range(0,numCourses)]       #邻接表
        for e in prerequisites: 
            b,a=e[0],e[1]               #[b,a]表示a是b的先修课程
            adj[a].append(b)
            indegree[b]+=1              #存在边<a,b>，b的入度增1
        st=deque()      #定义一个栈st
        for i in range(0,numCourses):       #入度为0的顶点i进栈
            if indegree[i]==0:st.append(i)
        n=0         #累计拓扑序列的顶点个数
        while st:
            i=st.popleft()      #出栈顶点i
            n+=1
            for j in adj[i]:                                #找到i的所有邻接点j
                indegree[j]-=1                          #顶点j的入度减少1
                if indegree[j]==0:st.append(j)          #入度为0的顶点j进栈
        return n==numCourses
