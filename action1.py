class Action:		            #活动类
    def __init__(self,b,e):
        self.b=b                #活动起始时间
        self.e=e                #活动结束时间
    def __lt__(self,other):	    #指定按e递增排序
        if self.e<other.e:return True
        else:return False

def greedly(A):		                #贪心算法
    global flag
    n=len(A)
    flag=[False]*n      #初始化为False
    A.sort()            #按e递增排序
    preend=0;				              #前一个兼容活动的结束时间
    for i in range(0,n):
        if A[i].b>=preend:
            flag[i]=True		              #选择A[i]活动
            preend=A[i].e

def action(A):			#求解活动安排问题Ⅰ
    greedly(A)
    print("求解结果");
    print("  选取的活动:",end='')
    cnt=0
    for i in range(0,len(A)):
        if flag[i]:
            print("[%d,%d] "%(A[i].b,A[i].e),end='')
            cnt+=1
    print("\n  共%d个活动"%(cnt))

A=[Action(1,4),Action(3,5),Action(0,6),Action(5,7),Action(3,8),Action(5,9),Action(6,10),Action(8,11),Action(8,12),Action(2,13),Action(12,15)]
#print("A:",A)
#A=[Action(1,2),Action(3,5),Action(7,8),Action(1,8)]
#print(A)
action(A)