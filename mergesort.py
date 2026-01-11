class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1:return 0
        self.ans=0
        self.MergeSort1(nums,0,n-1)
        return self.ans

    def Merge(self,a,low,mid,high):	#归并两个相邻有序子序列
        a1=[]						#用做临时表
        i,j=low,mid+1													#i、j分别为两个子表的下标
        while i<=mid and j<=high:						#在子表1和子表2均未遍历完时循环
            if a[i]<=a[j]:								#将子表1中的元素归并到a1
                a1.append(a[i]);i+=1
            else:											#将子表2中的元素归并到a1
                a1.append(a[j]);j+=1
                self.ans+=mid-i+1                           		#累计逆序数
        while i<=mid: 										#将子表1余下元素改变到a1
            a1.append(a[i]);i+=1
        while j<=high:										#将子表2余下元素改变到a1
            a1.append(a[j]);j+=1
        i=low
        for x in a1: 							            #将a1复制回a中
            a[i]=x;i+=1

    def MergeSort1(self,a,low,high):	        #二路归并排序
        if low<high:					#子序列有两个或以上元素
            mid=(low+high)//2			#取中间位置
            self.MergeSort1(a,low,mid)		#对a[low..mid]子序列排序
            self.MergeSort1(a,mid+1,high)	#对a[mid+1..high]子序列排序
            self.Merge(a,low,mid,high)		#将两有序子序列合并