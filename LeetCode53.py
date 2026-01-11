lass Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n,maxsum,cursum=len(nums),nums[0],0
        for i in range(0,n):
            cursum+=nums[i]
            maxsum=max(maxsum,cursum)		#通过比较求最大maxsum
            if cursum<0:cursum=0	        #若cursum<0，最大连续子序列从下一个位置开始
        return maxsum