class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        dq=deque()                  #定义一个双端队列dq
        ans=[]
        for i in range(0,n):            #处理nums中剩余的元素
            while len(dq)>0 and nums[i]>nums[dq[-1]]:
                dq.pop()               #将队尾小于nums[i]的元素从队尾出队
            dq.append(i)               #将元素下标i进队尾
            if i-dq[0]>=k:                  #将队头过期的元素从队头出队
                dq.popleft()
            if i>=k-1:              #i>=k-1时对应一个窗口
                ans.append(nums[dq[0]])           #新队头元素添加到ans中
        return ans
