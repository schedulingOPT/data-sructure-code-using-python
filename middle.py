def midnum1(a,i,b,j,n): 	            #求a[i]和b[j]开头长度为n的中位数
    if n==1:										#两序列均只有一个元素时返回较小者
        return min(a[i],b[j])
    else:												#两序列均含两个及以上素时
        m1=i+(n-1)//2									#求a的中位数
        m2=j+(n-1)//2									#求b的中位数
        if a[m1]==b[m2]:return a[m1]					#两中位数相等时返回该中位数
        newn=(n+1)//2									#保留的元素个数
        if a[m1]<b[m2]:									#当a[m1]<b[m2]时
            return midnum1(a,i+n-newn,b,j,newn)	#a取后半部分,b取前半部分
        else:									#当a[m1]>b[m2]时
            return midnum1(a,i,b,j+n-newn,newn) #a取前半部分,b取后半部分
def midnum(a,b,n):					            #求两个有序序列a和b的中位数
    return midnum1(a,0,b,0,n)


a=[11,13,15,17,19]
b=[2,4,6,8,20]
print("ans=",midnum(a,b,len(a)))
