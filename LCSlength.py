def LCSlength(a,b):					#求dp
    global dp
    m,n=len(a),len(b)
    dp=[[0]*(n+1) for i in range(m+1)]
    dp[0][0]=0
    for i in range(m+1):				#将dp[i][0]置为0,边界条件
        dp[i][0]=0
    for j in range(0,n+1):			#将dp[0][j]置为0,边界条件
        dp[0][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):		#两重for循环处理a、b的所有字符
            if a[i-1]==b[j-1]:			#情况(1)
                dp[i][j]=dp[i-1][j-1]+1
            else:						#情况(2)
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

def getasubs(a,b):	#由dp构造subs
    subs=""					#存放一个LCS
    m,n=len(a),len(b)
    k=dp[m][n]					#k为a和b的最长公共子序列长度
    i,j=m,n
    while k>0:						#在subs中放入最长公共子序列(反向)
        #print("i=%d,j=%d  "%(i,j))
        if dp[i][j]==dp[i-1][j]:
            i-=1
            #print("i--, i=",i)
        elif dp[i][j]==dp[i][j-1]:
            j-=1
            #print("j--, j=",j);
        else:
            subs+=a[i-1]		#subs中添加a[i-1]
            i,j,k=i-1,j-1,k-1
            #print("添加%c i--,j--, i=%d,j=%d"%(a[i],i,j))
    ans=list(subs)
    ans.reverse()
    return "".join(ans)	    #返回逆置subs的字符串

def solve(a,b):                 #求解算法
    print("求解结果")
    print("    LCS的长度:",LCSlength(a,b))
    print("    一个LCS:",getasubs(a,b))


def LCSlength1(a,b):	#求LCS的改进算法
    m,n=len(a),len(b)
    dp=[0]*(n+1)							#一维动态规划数组
    for i in range(1,m+1):
        upleft=dp[0]       					#阶段i初始化upleft
        for j in range(1,n+1):
            tmp=dp[j]      					#临时保存dp[j]
            if a[i-1]==b[j-1]:
                dp[j]=upleft+1
            else:
                dp[j]=max(dp[j-1],dp[j])
                upleft=tmp     			    #修改upleft
    return dp[n]

def solve1(a,b):                 #求解算法
    print("求解结果")
    print("    LCS的长度:",LCSlength1(a,b))


a="abcbdb"
b="acbbabdbb"
solve(a,b)
