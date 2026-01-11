def maxSubSum(a):   #求最大连续子序列和
    global dp
    n=len(a)
    dp=[0]*n
    dp[0]=a[0]
    for i in range(1,n):
        dp[i]=max(dp[i-1]+a[i],a[i])
    ans=max(dp)             #求dp中最大元素
    return max(ans,0)
    
def maxSub(a):	#求一个最大连续子序列 
    n=len(a)
    x=[]                    #存放一个最大连续子序列
    maxi=dp.index(max(dp))  #最大dp元素下标
    rsum=dp[maxi]
    i=maxi
    while i>=0 and rsum!=0:
        rsum-=a[i]
        x.append(a[i])
        i-=1
    x.reverse()
    return x

def solve(a):	    #输出结果
    ans=maxSubSum(a)
    print("求解结果")
    print("  最大连续子序列和:",ans)
    if ans==0:
        print("  所选子序列为空")
    else:	
        print("  dp: ",dp)
        x=maxSub(a)
        print("  所选子序列: ",x)

def maxSubSum1(a):		#求最大连续子序列和	
    n=len(a)
    if n==1:return a[0]
    dp=a[0]
    ans=dp
    for j in range(1,n):
        dp=max(dp+a[j],a[j])
        ans=max(ans,dp)
    return max(ans,0)

def solve1(a):		#输出结果 
    ans=maxSubSum1(a)
    print("求解结果")
    print("  最大连续子序列和: ",ans)

a=[-2,11,-4,13,-5,-2]
#a=[-1,3,-2,4]
#a=[-2,-1]
print("基本解法：")
solve(a)
print("空间优化：")
solve1(a)
