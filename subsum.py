cnt=0							#累计解个数
sum=0                           #累计搜索的结点个数
def disp(a):					#输出一个解
    global cnt,x
    cnt+=1;print("  第%d个解,"%(cnt),end='')
    print("选取的数为: ",end='')
    for i in range(0,len(x)):
        if x[i]==1:print(a[i],end=' ')
    print()
    
def dfs1(a,t,cs,i): 		#递归算法
    global sum,x
    sum+=1
    if i>=len(a):					#到达一个叶子结点
        if cs==t:disp(a)			#找到一个满足条件的解,输出
    else:							#没有到达叶子结点
        x[i]=1						#选取整数a[i]
        dfs1(a,t,cs+a[i],i+1)
        x[i]=0						#不选取整数a[i]
        dfs1(a,t,cs,i+1)

def subs1(a,t):						#求解子集和问题
    global x
    x=[0]*len(a)		    	    #解向量
    print("求解结果")
    dfs1(a,t,0,0)        #i从0开始
    print("sum=",sum)


def dfs2(a,t,cs,i): 		#递归算法
    global sum,x
    sum+=1
    if i>=len(a):										#到达一个叶子结点
      if cs==t:disp(a)										#找到一个满足条件的解,输出
    else:												#没有到达叶子结点
        if cs+a[i]<=t:									#左孩子结点剪支
            x[i]=1											#选取整数a[i]
            dfs2(a,t,cs+a[i],i+1)
        x[i]=0											#不选取整数a[i]
        dfs2(a,t,cs,i+1)

def subs2(a,t):						#求解子集和问题
    global x
    x=[0]*len(a)		    	    #解向量
    print("求解结果")
    dfs2(a,t,0,0)        #i从0开始
    print("sum=",sum)


def dfs3(a,t,cs,rs,i):		#递归算法
    global sum,x
    sum+=1
    if i>=len(a):						#到达一个叶子结点
        if cs==t:disp(a)				#找到一个满足条件的解,输出
    else:								#没有到达叶子结点
        rs-=a[i];						#求剩余的整数和
        if cs+a[i]<=t:					#左孩子结点剪支
            x[i]=1						#选取整数a[i]
            dfs3(a,t,cs+a[i],rs,i+1)
        if cs+rs>=t:				    #右孩子结点剪支
            x[i]=0					    #不选取整数a[i]
            dfs3(a,t,cs,rs,i+1)
        rs+=a[i]						#恢复剩余整数和(回溯)

def subs3(a,t):						#求解子集和问题
    global x
    x=[0]*len(a)		    	    #解向量
    rs=0
    for e in a:rs+=e
    print("求解结果")
    dfs3(a,t,0,rs,0)        #i从0开始
    print("sum=",sum)

a=[3,1,5,2]							#存放所有整数
t=8
subs2(a,t)
