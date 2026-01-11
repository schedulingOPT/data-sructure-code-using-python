def insertpoint1(a,k):			#查找第一个大于等于k的元素位置
    low,high=0,len(a)-1
    while low<=high:			#当前区间至少有一个元素时
        mid=(low+high)//2		#求查找区间的中间位置
        if k<=a[mid]:			#k<=a[mid]
            high=mid-1			#在R[low..mid-1]中查找,low不变
        else:
            low=mid+1			#在R[mid+1..high]中查找
    return low				    #返回low或high+1

def insertpoint2(a,k):			#查找第一个大于等于k的元素位置
    low,high=0,len(a)
    while low<high:			    #查找区间至少含两个元素
        mid=(low+high)//2
        if k<=a[mid]:			#k<=a[mid]
            high=mid		    #在左区间中查找(含a[mid])
        else:
            low=mid+1			#在右区间中查找
    return low					#返回low


a=[1,2,2,4]
k=5
print("算法1:%d的插入点为%d"%(k,insertpoint1(a,k)))
print("算法2:%d的插入点为%d"%(k,insertpoint2(a,k)))

