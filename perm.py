import copy
def Insert(s,i,j):			#在s的位置j插入i
    tmp=copy.deepcopy(s)
    tmp.insert(j,i)                          #位置j插入整数i
    return tmp

def CreatePi(s,i):		#在s集合中i-1到0位置插入i
    tmp=[]
    for j in range(len(s),-1,-1):                 #在s(含i-1个整数)的每个位置插入i
        s1=Insert(s,i,j)
        tmp.append(s1)                      	                #s1添加到Pi中
    return tmp

#***递归算法*********************************************/ 
def perm11(n,i): 	      #递归算法
    if i==1:
        return [[1]]
    else:
        Pi=[]			#存放1～i的全排列
        Pi_1=perm11(n,i-1)			  #求出Pi_1 
        for x in  Pi_1:
            tmp1=CreatePi(x,i)  	#在x集合中插入i得到tmp1
            for y in tmp1:Pi.append(y)	      #将tmp1的全部元素添加到Pi中
    return Pi

def perm1(n): 						  #递归法求1-n的全排列
    return perm11(n,n)


#***迭代算法*********************************************/ 
def perm2(n): 							  #迭代法求1-n的全排列
    Pi=[[1]]			    #Pi存放1～i的全排列,先置为{{1}}
    for i in range(2,n+1):                     	  #循环添加2～n
        Pi_1=copy.deepcopy(Pi)														  #新值取代旧值
        Pi.clear()
        for x in Pi_1:
            tmp1=CreatePi(x,i)  	  #在x集合中插入i得到tmp1
            for y in tmp1:Pi.append(y)	                #将tmp1的全部元素添加到Pi中
    return Pi

n=3
ans=perm2(n)
for x in ans:print(x,end=' ')