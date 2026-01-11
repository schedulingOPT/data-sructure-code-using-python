class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n,ans=len(nums),[]
        if n<3:return ans      					#长度小于3，返回空表
        nums.sort()              						#对nums递增排序
        if nums[0]>0:return ans     					#首元素大于0，返回空表
        for i in range(0,n-2):   				#遍历nums[i]
            if i>0 and nums[i]==nums[i-1]:	#跳过重复的元素nums[i]
                continue;
            low,high=i+1,n-1
            while low<high:
                sum=nums[low]+nums[high]
                if sum<-nums[i]:low+=1                   				#和太小，向右移动
                elif sum>-nums[i]:high-=1              				#和太大，向左移动
                else:                          							#找到一个三元组tmp
                    tmp=[nums[i],nums[low],nums[high]]
                    ans.append(tmp)           						#将tmp添加到ans中
                    low+=1
                    while low<high and nums[low]==nums[low-1]:	#跳过重复的元素nums[low]
                        low+=1
                    high-=1
                    while low<high and nums[high]==nums[high+1]: #跳过重复的元素nums[high]
                        high-=1
        return ans