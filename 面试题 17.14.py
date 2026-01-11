class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        ans=[0]*k
        if n==0 or k==0:return ans
        if n==k:return arr;
        self.QuickSelect(arr,0,n-1,k)
        for i in range(0,k):
            ans[i]=arr[i]
        return ans

    def Partition(self,a,s,t): 	#划分算法1
        i,j=s,t
        base=a[s]							#以表首元素为基准
        while i<j:								#从表两端交替向中间遍历,直至i=j为止
            while j>i and a[j]>=base:
                j-=1							#从后向前遍历,找一个小于等于基准的a[j]
            if j>i:
                a[i]=a[j]						#a[j]前移覆盖a[i]
                i+=1
            while i<j and a[i]<=base:
                i+=1						#从前向后遍历,找一个大于基准的a[i]
            if i<j:
                a[j]=a[i];					#a[i]后移覆盖a[j]
                j-=1
        a[i]=base								#基准归位
        return i								#返回归位的位置

    def QuickSelect(self,a,s,t,k):	
        if s<t: 										#至少存在2个元素的情况
            i=self.Partition(a,s,t)			#可以使用前面两种划分算法中的任意一种
            if k-1==i:
                return a[i]
            elif k-1<i:
                return self.QuickSelect(a,s,i-1,k)			#在左子序列中递归查找
            else:
                return self.QuickSelect(a,i+1,t,k)			#在右子序列中递归查找
