def maxSubSum1(a):								#解法1
    n,maxsum=len(a),0
    for i in range(0,n):					#两重循环穷举所有的连续子序列
        for j in range(i,n):
            cursum=0;
            for k in range(i,j+1):cursum+=a[k]
            maxsum=max(maxsum,cursum);	#通过比较求最大maxsum
    return maxsum

def maxSubSum2(a):					#解法2
    n=len(a)
    presum=[0]*(n+1)
    presum[0]=0
    for i in range(1,n+1):
        presum[i]=presum[i-1]+a[i-1]
    maxsum=0
    for  i in range(0,n):
        for j in range(i+1,n+1):
            cursum=presum[j]-presum[i]
            maxsum=max(maxsum,cursum);	#通过比较求最大maxsum
    return maxsum

def maxSubSum3(a):				#解法3
    n,maxsum=len(a),0
    for i in range(0,n):
        cursum=0
        for j in range(i,n):
            cursum+=a[j]
            maxsum=max(maxsum,cursum)	#通过比较求最大maxsum
    return maxsum

def maxSubSum4(a):				#解法4
    n,maxsum,cursum=len(a),0,0
    for i in range(0,n):
        cursum+=a[i];
        maxsum=max(maxsum,cursum)		#通过比较求最大maxsum
        if cursum<0:cursum=0	        #若cursum<0，最大连续子序列从下一个位置开始
    return maxsum
    
a=[-6,2,4,-7,5,3,2,-1,6,-9,10,-2]
print(maxSubSum4(a))
