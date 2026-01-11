class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxpq=[]        #大根堆
       	for i in range(0,len(stones)):
            heapq.heappush(maxpq,-stones[i])        #所有石头进队
        x,y=0,0
        while maxpq:
            x=-heapq.heappop(maxpq)
            if not maxpq:return x                  #若x是最后的石头，返回x
            y=-heapq.heappop(maxpq)                 #若x不是最后石头，则再出队y
            heapq.heappush(maxpq,-(x-y))            #粉碎后新重量为 x-y(x≥y)
        return x
