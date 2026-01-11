class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return nums[0]
        c,cnt=nums[0],1
        i=1
        while i<n:
            if nums[i]==c:                   #选择两个元素(R[i],c)
                cnt+=1                       #相同时累加次数
            else:
                cnt-=1                  #不相同时递减cnt，相当于删除这两个元素
                if cnt==0:            #cnt为0时对剩余元素从头开始查找
                    i+=1
                    c=nums[i];cnt+=1
            i+=1
        return c
