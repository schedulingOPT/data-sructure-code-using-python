def Sum1(n,s):
    if n<=0:return False	    	#参数错误时返回假
    for i in range(1,n+1):s+=i
    return True				      	#参数正确时计算出结果并返回真

def Sum2(n,sl):
    if n<=0:return False	    	#参数错误时返回假    
    sl[0]=0
    for i in range(1,n+1):sl[0]+=i
    return True				      	#参数正确时计算出结果并返回真

def Sum3(n):
    s=0
    for i in range(1,n+1):s+=i
    return s

def Sum4(n):
	return n(n+1)//2

n,b=10,[0]
ret=Sum2(n,b)
print("ret:%s,b:%d"%(ret,b[0]))
