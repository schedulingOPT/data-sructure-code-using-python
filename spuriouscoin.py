def Balance(c,ia,ib,n):			#c[ia]和c[ib]开始的n个硬币称重一次
    sa,sb=0,0
    i=ia
    for j in range(0,n):sa+=c[i];i+=1
    i=ib
    for j in range(0,n):sb+=c[i];i+=1
    if sa<sb:return 1					    #A轻
    elif sa==sb:return 0					#A，B重量相同
    else:return -1							#B轻

def spcoin1(coins,i,n):			#在coins[i..i+n-1](共n个硬币)中查找假币
    if n==1:return i						#剩余1个硬币coins[i]
    elif n==2:							#剩余2个硬币coins[i]和coins[i+1]
        b=Balance(coins,i,i+1,1)			    #2个硬币称重
        if b==1:return i					#coins[i]是假币
        else:return i+1						#coins[i+1]是假币
    else:								#剩余3个或者以上硬币coins[i..i+n-1]
        k=0							#k为A和B中的硬币个数
        if n%3==0:k=n//3
        elif n%3==1:k=n//3
        else:k=n//3+1
        ia,ib,ic=i,i+k,i+2*k							#分为A,B,C,硬币个数分别为,k,n-2k
        b=Balance(coins,ia,ib,k)						#A,B称重一次
        if b==0:return spcoin1(coins,ic,n-2*k)  #A,B的重量相同，假币在C中
        elif b==1:return spcoin1(coins,ia,k)			#A轻，假币A中
        else:return spcoin1(coins,ib,k)					#B轻，假币在B中

def spcoin(coins):	  				#求解算法：在coins中查找较轻的假币
    return spcoin1(coins,0,len(coins))

n=25
c=[2]*n             #存放所有的硬币
c[15]=1				#指定编号i为假币
print("求解结果")
print("    假币为",spcoin(c))