class Solution:
    hmap={} 	    #定义哈希表作为动态规划数组
    def rob(self, root: Optional[TreeNode]) -> int:
        if root==None:return 0
        return self.dfs(root)

    def dfs(self,root):              							 #递归算法
        if root==None:return 0
        if root in self.hmap:return self.hmap[root]		#该子问题已经求出，直接返回解
        money1=root.val
        if root.left:
            money1+=self.dfs(root.left.left)+self.dfs(root.left.right)
        if root.right:
            money1+=self.dfs(root.right.left)+self.dfs(root.right.right)
        money2=self.dfs(root.left)+self.dfs(root.right)
        self.hmap[root]=max(money1,money2)				#将子问题的解存放到hmap中
        return self.hmap[root]


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
       	if root==None:return 0
        dp=self.dfs(root)
        return max(dp[0],dp[1])

    def dfs(self,root):            				#动态规划算法
        dp=[0,0]
        if root==None:return dp
        ldp=self.dfs(root.left)
        rdp=self.dfs(root.right)
        dp[0]=max(ldp[0],ldp[1])+max(rdp[0],rdp[1])
        dp[1]=root.val+ldp[0]+rdp[0]
        return dp
