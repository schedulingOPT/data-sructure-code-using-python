def f1(n):							#算法1
	if n==1:return 1
	elif n==2:return 2
	else:return f1(n-2)+f1(n-1)



def f21(n):						#被f2调用
	if dp[n]!=0:return dp[n]
	if n==1:dp[n]=1
	elif n==2:dp[n]=2
	else:dp[n]=f21(n-2)+f21(n-1)
	return dp[n]

def f2(n):							#算法2
    global dp
    dp=[0]*105
    return f21(n)

def f3(n):							#算法3
    dp=[0]*105
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[n]

def f4(n):							#算法4
    dp=[0]*3
    dp[0],dp[1]=1,2
    for i in range(2,n):
        dp[i%3]=dp[(i-1)%3]+dp[(i-2)%3]
    return dp[(n-1)%3]

def f5(n):							#算法5
    if n==1:return 1
    elif n==2:return 2
    else:
        a,b,c=1,2,0
        for i in range(3,n+1):
            c=a+b
            a,b=b,c
    return c


n=5
print("f1:",f1(n))
print("f2:",f2(n))
print("f3:",f3(n))
print("f4:",f4(n))
print("f5:",f5(n))

