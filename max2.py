INF=0x3f3f3f3f
def max21(a,low,high):   #被max2调用
    ans=[0,0]
    if low==high:		#区间只有一个元素
        ans[0],ans[1]=a[low],-INF
    elif low==high-1:	#区间只有两个元素
        ans[0],ans[1]=max(a[low],a[high]),min(a[low],a[high])
    else:
        mid=(low+high)//2
        leftans=max21(a,low,mid)		#左区间求leftans
        rightans=max21(a,mid+1,high)	#右区间求rightans
        if leftans[0]>rightans[0]:
            ans[0]=leftans[0]
            ans[1]=max(leftans[1],rightans[0]);	#合并求次大元素
        else:
            ans[0]=rightans[0]
            ans[1]=max(leftans[0],rightans[1])  #合并求次大元素
    return ans

def max2(a):        #求a中最大和次大元素 
    return max21(a,0,len(a)-1)

a=[1,2,3]
ans=max2(a)
print("max1=%d,max2=%d"%(ans[0],ans[1]))
