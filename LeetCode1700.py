class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n=len(students)
        qu=deque()          #定义一个队列qu
        st=deque()          #定义一个栈st
        for x in students:                                  #建立学生队列
            qu.append(x)
        for i in range(n-1,-1,-1):      #建立三明治栈
            st.append(sandwiches[i])
        i=n
        while i>0:
            if st[-1]==qu[0]:                       #队列最前面学生喜欢栈顶三明治
                st.pop();qu.popleft()
                n-=1                                                #子问题的人数减少1
                i=n                                             #重置i
            else:                                                   #否则
                tmp=qu[0]; qu.popleft()                         #出队后进入队尾
                qu.append(tmp)
                i-=1                                                #操作次数减少1
        return len(st)
