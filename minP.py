from operator import itemgetter,attrgetter
def greedly(a):      					#贪心算法
    n=len(a)
    maxd=0
    for i in range(0,n):maxd=max(maxd,a[i][0])
    days=[False]*(maxd+1)
    a.sort(key=itemgetter(1),reverse=True)  #按惩罚值递减排序
    ans=0
    for i in range(0,n):
        j=a[i][0]
        while j>0:				#查找截止日期之前的空时间
            if not days[j]: 	#找到空时间
                days[j]=True
                print("  作业[%d,%d]在第%d天完成"%(a[i][0],a[i][1],j))
                break
            j-=1
        if j==0:				#没有找到空时间
            ans+=a[i][1]		#累计惩罚值
            print("  不能完成作业[%d,%d],惩罚%d"%(a[i][0],a[i][1],a[i][1]))
    return ans

def solve(a):
    print("求解结果")
    ans=greedly(a)
    print("  总惩罚值=",ans)
    
a=[[4,70],[2,60],[4,50],[3,40],[1,30],[4,20],[6,10]]
solve(a)