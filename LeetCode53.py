class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        return self.maxSubSum51(nums,0,n-1)

    def maxSubSum51(self,nums,low,high): 			#被maxSubSum3调用
        if low==high:return nums[low]          			#子序列只有一个元素时
        mid=(low+high)//2                            	#求中间位置
        maxLeftSum=self.maxSubSum51(nums,low,mid)          #求左边的最大连续子序列之和
        maxRightSum=self.maxSubSum51(nums,mid+1,high)  #求右边的最大连续子序列之和
        maxLeftBorderSum,lowBorderSum=nums[mid],0
        for i in range(mid,low-1,-1):             	#求nums[i..mid]的最大连续子序列和
            lowBorderSum+=nums[i]
            maxLeftBorderSum=max(maxLeftBorderSum,lowBorderSum)
        maxRightBorderSum,highBorderSum=nums[mid+1],0
        for j in range(mid+1,high+1):    		#求nums[mid+1..j]的最大连续子序列和
            highBorderSum+=nums[j]
            maxRightBorderSum=max(maxRightBorderSum,highBorderSum)
        ans=max(max(maxLeftSum,maxRightSum),maxLeftBorderSum+maxRightBorderSum)
        return ans