def BinSearch11(a,low,high,k):      #被BinSearch1调用
    if low<=high:				#当前区间存在元素时
        mid=(low+high)//2		#求查找区间的中间位置
        if k==a[mid]:			#找到后返回下标mid
            return mid
        elif k<a[mid]:			#当k<a[mid]时,在左区间中递归查找
            return BinSearch11(a,low,mid-1,k)
        else:					#当k>a[mid]时,在右区间中递归查找
            return BinSearch11(a,mid+1,high,k)
    else:return -1			#若当前查找区间为空时返回-1

def BinSearch1(a,k): 	#递归二分查找算法
    return BinSearch11(a,0,len(a)-1,k)

def BinSearch2(a,k):        #二分查找迭代算法Ⅰ
    low,high=0,len(a)-1
    while low<=high:        #当前区间存在元素时循环
        mid=(low+high)//2		#求查找区间的中间位置
        if k==a[mid]:			#找到后返回其下标mid
            return mid
        elif k<a[mid]:			#当k<a[mid]时,在左区间中递归查找
            high=mid-1
        else:					#当k>a[mid]时,在右区间中递归查找
            low=mid+1
    return -1					#若当前查找区间没有元素时返回-1

def BinSearch3(a,k):	#二分查找迭代算法Ⅱ
    low,high=0,len(a)-1
    while low<high:		#当前区间存在两个或更多元素时循环
        mid=(low+high)//2		#求查找区间的中间位置
        if a[mid]>=k:			#当k<a[mid]时,在左区间中递归查找
            high=mid
        else:					#当k>a[mid]时,在右区间中递归查找
            low=mid+1
    if a[low]==k:
        return low         #成功查找
    else:
        return -1					#返回-1

def BinSearch4(a,k):        #二分查找迭代算法Ⅲ
    low,high=0,len(a)-1
    while low+1<high:   	#当前区间存在3个或更多元素时循环
        mid=(low+high)//2		#求查找区间的中间位置
        if a[mid]<k:			#当k<a[mid]时,在左区间中递归查找
            low=mid;
        else:					#当k>a[mid]时,在右区间中递归查找
            high=mid;
    if a[low]==k:
        return low         #成功查找
    elif a[high]==k:
        return high
    else:
        return -1					#返回-1

a=[1,2,4,5,7,8,10]
for i in range(0,len(a)):
    k=a[i]
    i=BinSearch4(a,k)
    if i>=0:
        print("a[%d]=%d"%(i,k))
    else:
        print("未找到%d元素"%(k))
