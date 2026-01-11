class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        dp=nums[0]
        ans=dp
        for j in range(1,n):
            dp=max(dp+nums[j],nums[j])
            ans=max(ans,dp)
        return ans;            #不能改为max(ans,0)
