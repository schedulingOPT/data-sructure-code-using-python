class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=0x3f3f3f3f							#表示∞
        if amount==0:return 0
        n=len(coins)
        if n==1 and amount%coins[0]!=0:return -1
        dp=[INF]*(amount+1) 				#一维动态规划数组,初始化所有元素为∞
        dp[0]=0
        for i in range(1,n+1):
            for r in range(coins[i-1],amount+1):
                dp[r]=min(dp[r],dp[r-coins[i-1]]+1)
        return -1 if dp[amount]==INF else dp[amount]
