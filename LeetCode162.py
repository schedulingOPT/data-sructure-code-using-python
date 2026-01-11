class Solution:
    def findPeakElement(self, nums: List[int]) -> int:      #解法1
        n=len(nums)
        if n==1:return 0
        low,high=0,n-1
        while low<=high:                    #查找区间至少有一个元素时循环
            mid=(low+high)//2
            if mid+1>=n or nums[mid]>nums[mid+1]:    #峰值在左边
              	high=mid-1
            else:                           #峰值在右边
              	low=mid+1
        return low

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:      #解法2
        n=len(nums)
        if n==1:return 0
        low,high=0,len(nums)
        while low<high:                    #查找区间至少有一个元素时循环
            mid=(low+high)//2
            if mid+1>=n or nums[mid]>nums[mid+1]:    #峰值在左边
              	high=mid
            else:                           #峰值在右边
              	low=mid+1
        return low
