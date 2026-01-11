def maxSubSum51(a,low,high):				#分治算法
    if low==high:return max(a[low],0)		#子序列只有一个元素时
    mid=(low+high)//2												#求中间位置
    maxLeftSum=maxSubSum51(a,low,mid)				#求左边的最大连续子序列之和
    maxRightSum=maxSubSum51(a,mid+1,high)		#求右边的最大连续子序列之和
    maxLeftBorderSum,lowBorderSum=0,0
    for i in range(mid,low-1,-1):										#求左段a[i..mid]的最大连续子序列和
        lowBorderSum+=a[i]
        maxLeftBorderSum=max(maxLeftBorderSum,lowBorderSum)
    maxRightBorderSum,highBorderSum=0,0
    for j in range(mid+1,high+1):								#求右段a[mid+1..j]的最大连续子序列和
        highBorderSum+=a[j]
        maxRightBorderSum=max(maxRightBorderSum,highBorderSum)
    return max(max(maxLeftSum,maxRightSum),maxLeftBorderSum+maxRightBorderSum)

def maxSubSum5(a):							#求a序列中最大连续子序列和
    return maxSubSum51(a,0,len(a)-1)

a=[-6,2,4,-7,5,3,2,-1,6,-9,10,-2]
print(maxSubSum5(a))
