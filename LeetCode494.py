class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ans=0
        self.dfs(nums,target,0,0)
        return self.ans

    def  dfs(self,nums,target,i,expv):	#回溯算法
        if i==len(nums):					#到达一个叶子结点
            if expv==target:self.ans+=1				#找到一个解
        else:
            expv+=nums[i]									#nums[i]前选择'+'
            self.dfs(nums,target,i+1,expv)
            expv-=nums[i]										#回溯：恢复expv
            expv-=nums[i]										#nums[i]前选择'-'
            self.dfs(nums,target,i+1,expv)
            expv+=nums[i]										#回溯：恢复expv