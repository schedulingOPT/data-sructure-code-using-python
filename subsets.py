import copy
def appendi(Mi_1,e):	#向Mi_1中每个集合元素末尾添加e
    Ai=Mi_1
    for x in Ai:x.append(e)
    return Ai  

def subsets(n): 	#迭代法：求1-n的幂集
    Mi_1=[[],[1]]            #Mi_1初始化为1的幂集
    if n==1:return Mi_1						#处理特殊情况
    for i in range(2,n+1):
        Mi=copy.deepcopy(Mi_1)
        Ai=appendi(Mi_1,i)
        for x in Ai:Mi.append(x)    		    #将Ai所有集合元素添加到Mi中
        Mi_1=copy.deepcopy(Mi)
    return Mi

n=3
ans=subsets(n)
for x in ans:print(x,end=' ')