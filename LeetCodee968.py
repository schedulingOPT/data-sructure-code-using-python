class Solution:
    INF=0x3f3f3f3f
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        dp=self.dfs(root)
        return min(dp[0],dp[1])

    def dfs(self,root):
        dp=[0,0,0] 
        if root==None:
            dp[0]=self.INF	#无法安装摄影头
            dp[1]=0				#可以认为能覆盖
            dp[2]=self.INF			#与dp[1]的情况相反
            return dp
        ldp=self.dfs(root.left); 
        rdp=self.dfs(root.right); 
        dp[0]=min(ldp[0],min(ldp[1],ldp[2]))+min(rdp[0],min(rdp[1],rdp[2]))+1
        dp[1]=min(ldp[0]+min(rdp[0],rdp[1]),rdp[0]+min(ldp[0],ldp[1]))
        dp[2]=ldp[1]+rdp[1]
        return dp
