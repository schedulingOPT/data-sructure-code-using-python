MAXN=20                    #最多皇后个数
q=[0]*MAXN                 	#q[i]存放第i个皇后的列号
class Solution:
    def totalNQueens(self, n: int) -> int:
        self.cnt=0                      #累计解个数
        self.dfs(1,n)
        return self.cnt

    def place(self,i,j):                 #测试(i,j)位置能否摆放皇后
        if i==1: return True	        #第一个皇后总是可以放置
        k=1
        while k<i:					 	#k=1～i-1是已放置了皇后的行
            if q[k]==j or (abs(q[k]-j)==abs(i-k)):
                return False
            k+=1
        return True

    def dfs(self,i,n):			         	#放置1～i的皇后
        if i>n:                      	#所有皇后放置结束
            self.cnt+=1
        else:
            for j in range(1,n+1):			#在第i行上试探每一个列j
                if self.place(i,j):				#在第i行上找到一个合适位置(i,j)
                    q[i]=j
                    self.dfs(i+1,n)
