class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans=[];		#存放nums的全排列
        x=nums
        self.dfs(x,0)
        return self.ans

    def dfs(self,x,i):		#回溯算法
        if i==len(x):
            self.ans.append(copy.deepcopy(x))
        else:
            for j in range(i,len(x)):
                x[i],x[j]=x[j],x[i]
                self.dfs(x,i+1)
                x[i],x[j]=x[j],x[i]
