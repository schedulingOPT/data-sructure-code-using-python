class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:return matrix[0][0] 	# n=1为特殊情况，返回该元素
        dp=[[0]*n for i in range(n)]	#二维动态规划数组
        for j in range(0,n):       		#第0行:边界情况
            dp[0][j]=matrix[0][j]
        for i in range(1,n):
            for j in range(0,n):
                if j==0:dp[i][j]=min(dp[i-1][j],dp[i-1][j+1])+matrix[i][j]
                elif j==n-1:dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+matrix[i][j]
                else:dp[i][j]=min(dp[i-1][j-1],min(dp[i-1][j],dp[i-1][j+1]))+matrix[i][j]
        ans=min(dp[n-1])                  	#求dp第n-1行中的最小元素ans
        return ans



class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:return matrix[0][0] 	# n=1为特殊情况，返回该元素
        dp=[[0]*n for i in range(2)]	#二维动态规划数组
        for j in range(0,n):       		#第0行:边界情况
            dp[0][j]=matrix[0][j]
        c=0
        for i in range(1,n):
            c=1-c
            for j in range(0,n):
                if j==0:dp[c][j]=min(dp[1-c][j],dp[1-c][j+1])+matrix[i][j]
                elif j==n-1:dp[c][j]=min(dp[1-c][j-1],dp[1-c][j])+matrix[i][j]
                else:dp[c][j]=min(dp[1-c][j-1],min(dp[1-c][j],dp[1-c][j+1]))+matrix[i][j]
        ans=min(dp[c])                  	#求dp第c行中的最小元素ans
        return ans


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:return matrix[0][0]     # n=1为特殊情况，返回该元素
        dp=[[0]*n for i in range(n)]    #二维动态规划数组
        for j in range(0,n):             #第n-1行:边界情况
            dp[n-1][j]=matrix[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(0,n):
                if j==0:dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+matrix[i][j]
                elif j==n-1:dp[i][j]=min(dp[i+1][j],dp[i+1][j-1])+matrix[i][j]
                else:dp[i][j]=min(dp[i+1][j-1],min(dp[i+1][j],dp[i+1][j+1]))+matrix[i][j]
        ans=min(dp[0])
        return ans

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        if n==1:return matrix[0][0]     # n=1为特殊情况，返回该元素
        dp=[[0]*n for i in range(2)]    #二维动态规划数组
        c=0
        for j in range(0,n):            #第n-1行:边界情况
         	dp[c][j]=matrix[n-1][j]
        for i in range(n-2,-1,-1):
            c=1-c
            for j in range(0,n):
                if j==0:dp[c][j]=min(dp[1-c][j],dp[1-c][j+1])+matrix[i][j]
                elif j==n-1:dp[c][j]=min(dp[1-c][j],dp[1-c][j-1])+matrix[i][j]
                else:dp[c][j]=min(dp[1-c][j-1],min(dp[1-c][j],dp[1-c][j+1]))+matrix[i][j]
        ans=min(dp[c])
        return ans

