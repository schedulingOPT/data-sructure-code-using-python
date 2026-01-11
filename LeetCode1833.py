class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()					#默认递增排序
        ans=0
        rc=coins							#剩余的金额（从coins开始）
        for i in range(0,len(costs)):
            if costs[i]<=rc:				#可以买则买该雪糕
                ans+=1
                rc-=costs[i]
        return ans
