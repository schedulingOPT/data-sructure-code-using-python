def Partition1(a,s,t): 	#划分算法1
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

def Partition2(a,s,t):		#划分算法2
    i,j=s,s+1
    base=a[s]							#以表首元素为基准
    while j<=t:							#j从s+1开始遍历其他元素
        if a[j]<=base:					#找到小于等于基准的元素a[j]
            i+=1							#扩大小于等于base的元素区间
            if i!=j:
                a[i],a[j]=a[j],a[i]			#将a[i]与a[j]交换
        j+=1								#继续扫描
    a[s],a[i]=a[i],a[s]         			#将基准a[s]和a[i]进行交换
    return i

def QuickSort11(a,s,t):		#对R[s..t]的元素进行快速排序
    if s<t: 				 							#表中至少存在两个元素的情况
        i=Partition1(a,s,t)						#可以使用前面2种划分算法中的任意一种
        QuickSort11(a,s,i-1)						#对左子表递归排序
        QuickSort11(a,i+1,t)						#对右子表递归排序

def QuickSort1(a):				#递归算法：快速排序
	QuickSort11(a,0,len(a)-1)

a=[2,5,1,7,10,6,9,4,3,8]
print("a:",a)
QuickSort1(a)
print("a:",a)
