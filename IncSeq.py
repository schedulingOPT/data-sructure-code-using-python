def maxInclen(a):			#求最长递增子序列长度
    global dp
    n=len(a)
    dp=[0]*n
    for i in range(0,n):
        dp[i]=1
        for j in range(0,i):
            if a[i]>a[j]:dp[i]=max(dp[i],dp[j]+1)
    ans=max(dp)             #求dp中最大元素
    return ans

def maxInc(a):	                #求一个最长递增子序列
    n=len(a)
    x=[]            		        #存放一个最长递增子序列
    maxj=dp.index(max(dp))          #dp中最大元素下标
    rnum=dp[maxj]					#剩余的元素个数 
    j=maxj							#j指向当前最长递增子序列的一个元素 
    x.append(a[j])
    prej=maxj-1					    #prej查找最长递增子序列的前一个元素
    while prej>=0 and rnum!=0:
        if a[prej]<a[j] and dp[prej]==rnum-1:
            rnum-=1
            x.append(a[prej])
            j=prej
        prej-=1
    x.reverse()     #逆置x
    return x

def solve(a):       #求解算法
    print("求解结果")
    ans=maxInclen(a)
    print("   dp:")
    for i in range(0,len(a)):
        print("   dp[%d]=%d"%(i,dp[i]))
    print("   最长递增子序列的长度:",ans)
    x=maxInc(a)
    print("   一个最长递增子序列:",x)

a=[2,1,5,3,6,4,8,9,7]
#a=[1,2,1,8,9]
solve(a)
