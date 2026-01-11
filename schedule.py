INF=0x3f3f3f3f
def schedule1(a,b,n):				#求解算法1
    maxA,maxB=sum(a),sum(b)     #求maxA和maxB 
    dp=[[[False]*(maxB+1) for i in range(maxA+1)] for j in range(n+1)]	#三维动态规划数组
    for A in range(0,maxA+1):
        for B in range(0,maxB+1):
            dp[0][A][B]=True			#k=0时一定有解
    for k in range(1,n+1):
        for A in range(0,maxA+1):
            for B in range(0,maxB+1):
                if A-a[k-1]>=0:		#在MA上处理
                    dp[k][A][B]=dp[k-1][A-a[k-1]][B]
                if B-b[k-1]>=0:		#在MB上处理
                    dp[k][A][B]=(dp[k][A][B] or dp[k-1][A][B-b[k-1]])
    ans=INF						        #存放最少时间
    for A in range(0,maxA+1):				#求ans
        for B in range(0,maxB+1):
            if dp[n][A][B]:ans=min(ans,max(A,B))
    return ans
  
def schedule2(a,b,n):			#求解算法2
    maxA,maxB=sum(a),sum(b)     #求maxA和maxB 
    dp=[[[False]*(maxB+1) for i in range(maxA+1)] for j in range(2)]	#三维动态规划数组
    for A in range(0,maxA+1):
        for B in range(0,maxB+1):
            dp[1][A][B]=False			#k=1时初始化为false
            dp[0][A][B]=True			#k=0时一定有解
    c=0
    for k in range(1,n+1):
        c=1-c
        for  A in range(0,maxA+1):
            for B in range(0,maxB+1):	
                dp[c][A][B]=False         #初始化dp[c]为false
        for A in range(0,maxA+1):
            for B in range(0,maxB+1):
                if A-a[k-1]>=0:		#在MA上处理
                    dp[c][A][B]=dp[1-c][A-a[k-1]][B]
                if B-b[k-1]>=0:		#在MB上处理
                    dp[c][A][B]=(dp[c][A][B] or dp[1-c][A][B-b[k-1]])
    ans=INF						#存放最少时间
    for A in range(0,maxA+1):
        for B in range(0,maxB+1):
            if dp[c][A][B]:
                ans=min(ans,max(A,B))
    return ans

def schedule3(a,b,n):					#求解算法3
    maxA=sum(a)     #求maxA
    dp=[0]*(maxA+1)							#一维动态规划数组
    for k in range(1,n+1): 
        for A in range(maxA,-1,-1):
            if A<a[k-1]:						#此时只能在MB上运行
                dp[A]=dp[A]+b[k-1]
            else:								#否则取MA或者MB上处理的最少时间
                dp[A]=min(dp[A-a[k-1]],dp[A]+b[k-1])
    ans=INF										#存放最少时间
    for A in range(0,maxA+1):
        ans=min(ans,max(A,dp[A]))
    return ans

a=[2,5,7,10,5,2]
b=[3,8,4,11,3,4]
n=len(a)
print("解法1：ans=",schedule1(a,b,n))
print("解法2：ans=",schedule2(a,b,n))
print("解法3：ans=",schedule3(a,b,n))
