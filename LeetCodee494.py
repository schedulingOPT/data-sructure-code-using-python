class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n,s=len(nums),sum(nums)
        if target>s:return 0
        if (s-target)%2==1:return 0
        W=(s-target)//2
        dp=[[0]*(W+1) for i in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for r in range(0,W+1):
                if r<nums[i-1]:
                    dp[i][r]=dp[i-1][r]
                else:
                    dp[i][r]=dp[i-1][r-nums[i-1]]+dp[i-1][r]
        return dp[n][W]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n,s=len(nums),sum(nums)
        if target>s:return 0
        if (s-target)%2==1:return 0
        W=(s-target)//2
        dp=[0]*(W+1)
        dp[0]=1
        for i in range(1,n+1):
            for r in range(W,nums[i-1]-1,-1):   	#r按nums[i-1]到W的逆序
                dp[r]+=dp[r-nums[i-1]]              #组合总数是累计关系
        return dp[W]
