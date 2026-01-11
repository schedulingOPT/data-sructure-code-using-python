def greedly(c,k,A):	          		#贪心算法
    ans=0
    curm=2**k
    while A>0:
        curs=A//curm   		    #求面额为curm的硬币个数
        ans+=curs                      #累计硬币个数
        print("  面额为%d的硬币个数=%d"%(curm,curs))
        A-=curs*curm                   #剩余金额
        curm/=c;
    return ans

def solve(c,k,A):               #求解零钱兑换问题
    print("求解结果")
    print("兑换金额%d的最少硬币个数=%d"%(A,greedly(c,k,A)))

A=23
c=2
k=3
solve(c,k,A)
