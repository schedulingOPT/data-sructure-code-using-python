class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans,self.x=[],[]
        self.dfs(nums,0)
        return self.ans

    def dfs(self,nums,i):           #回溯算法
        if i==len(nums):                                    #到达一个叶子结点
            self.ans.append(copy.deepcopy(self.x))
        else:
            self.x.append(nums[i])                  #选择nums[i], x中添加nums[i]
            self.dfs(nums,i+1)
            self.x.pop()                                #回溯
            self.dfs(nums,i+1)              #不选择nums[i],x中不添加nums[i]
            
            

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root==None:return []
        self.ans=[]
        x=[];                           #存放一条路径
        x.append(root.val)
        self.dfs(root,x)                #dfs求ans
        return self.ans

    def dfs(self,root,x):               #回溯算法
        if root.left==None and root.right==None:    #找到一条路径
            tmp=str(x[0])                           #路径转换为字符串
            for i in range(1,len(x)):
                tmp+="->"+str(x[i])
            self.ans.append(tmp)
        else:
            if root.left!=None:
                x.append(root.left.val)
                self.dfs(root.left,x)
                x.pop()						#回溯
            if root.right!=None:
                x.append(root.right.val)
                self.dfs(root.right,x)
                x.pop()                         #回溯
            