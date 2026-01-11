class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k,i=0,0                                           #k记录结果数组中的元素个数
        while i<n:
            if nums[i]!=val:                            #nums[i]是保留的元素
                nums[i-k]=nums[i]                       #将nums[i]前移k个位置
            else:                                                   #nums[i]是要删除的元素
                k+=1                                            #k增1
            i+=1
        return n-k                                           #返回结果数组的长度n-k
