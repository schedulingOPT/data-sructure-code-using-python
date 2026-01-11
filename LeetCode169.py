class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        cntmap={}   #定义计数器cntmap
        for x in nums:
            if x in cntmap:cntmap[x]+=1
            else:cntmap[x]=1
        ans=0                                       #存放多数元素
        for x in cntmap: 
            cnt=cntmap[x]                           #获取x对应的计数
            if cnt>n//2:                            #找到多数元素
                ans=x
                break
        return ans
