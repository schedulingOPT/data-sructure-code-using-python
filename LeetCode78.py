class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Mi=[]                               #存放幂集
        Mi_1=[[],[nums[0]]]
        n=len(nums)
        if n==1:return Mi_1                 #处理特殊情况
        for i in range(1,n):
            Mi=copy.deepcopy(Mi_1)
            Ai=self.appendi(Mi_1,nums[i])
            for x in Ai:Mi.append(x)        #将Ai所有集合元素添加到Mi中
            Mi_1=copy.deepcopy(Mi)          #用新值替换旧值
        return Mi

    def appendi(self,Mi_1,e):               #向Mi_1中每个集合元素末尾添加e
        Ai=Mi_1                             #浅拷贝
        for x in Ai:x.append(e)
        return Ai
