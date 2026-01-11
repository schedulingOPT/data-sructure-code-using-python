class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()								    #nums递增排序
        self.ans,self.x=set(),[]
        self.dfs(nums,0)
        return list(self.ans)

    def dfs(self,nums,i):           			    #回溯算法
        if i==len(nums):                             #到达一个叶子结点
           	self.ans.add(tuple(self.x))
        else:
            self.x.append(nums[i])                  #选择nums[i], x中添加nums[i]
            self.dfs(nums,i+1)
            self.x.pop()                              #回溯
            self.dfs(nums,i+1)              		#不选择nums[i],x中不添加nums[i]


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ans,x=[],[]
        self.dfs(nums,x,0)
        return self.ans

    def dfs(self,nums,x,i):
        self.ans.append(copy.deepcopy(x))
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            x.append(nums[j])
            self.dfs(nums,x,j+1)
            x.pop()

