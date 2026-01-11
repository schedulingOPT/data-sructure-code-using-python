class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        k,i=-1,0                                           #k记录结果数组中的元素个数
        while i<n:
            if nums[i]!=val:                            #nums[i]是保留的元素
                k+=1                                            #扩大保留元素区间 
                nums[k],nums[i]=nums[i],nums[k]         #nums[]k]和nums[i]交换
            i+=1
        return k+1                                      #返回结果数组的长度k+1
