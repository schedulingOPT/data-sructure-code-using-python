def subsets1(a):				#解法1:求a的幂集
    x=[0]*len(a)		#解向量
    dfs1(a,x,0)

def dfs1(a,x,i):			    #回溯算法
    if i>=len(a):	        #到达一个叶子结点
        print("[",end='')
        for j in range(0,len(x)):
            if x[j]==1:
                print(a[j],end=' ')
        print("]",end='  ')
    else:
        x[i]=1;
        dfs1(a,x,i+1)		#选择a[i]
        x[i]=0
        dfs1(a,x,i+1);		#不选择a[i]

def subsets2(a):		    #解法2:求a的幂集
    x=[]		            #解向量
    dfs2(a,x,0)

def dfs2(a,x,i):	        #回溯算法
    print(x,end='  ')
    for j in range(i,len(a)):
        x.append(a[j])      #向x中添加a[j]
        dfs2(a,x,j+1)
        x.pop()			    #回溯即删除前面添加的a[j]

a=[1,2,3]
print("解法1:")
subsets1(a)
print()
print("解法2:")
subsets2(a)