class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
     	n=len(nums)
        	k,i=0,0                                           		#k记录结果数组中的元素个数
        	while i<n:
            	if nums[i]!=val:                             	#nums[i]是保留的元素
                	nums[k]=nums[i];                    	#将nums[i]重新插入到结果数组中
                	k+=1                        					#结果数组的长度增1
            	i+=1
        	return k                                        		#返回保留的元素个数
