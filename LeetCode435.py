class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        INF=0x3f3f3f3f								#表示∞
        n=len(intervals)
        if n<=1:return 0
        intervals.sort(key=itemgetter(1))   #按区间终点递增排序
        ans=0     					#表示兼容区间的个数
        preend=-INF
        for i in range(0,n):
            if intervals[i][0]>=preend:
               	ans+=1
                preend=intervals[i][1]
       	return n-ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        INF=0x3f3f3f3f                              #表示∞
        n=len(intervals)
        if n<=1:return 0
        intervals.sort(key=itemgetter(1))       #按区间终点递增排序
        ans=0                                   #表示兼容区间的个数
        preend=-INF
        for i in range(0,n):
            if intervals[i][0]<preend:          #找到一个相交区间
                ans+=1
            else:
                preend=intervals[i][1]              #重置preend
        return ans
