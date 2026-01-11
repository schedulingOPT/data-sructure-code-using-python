def Bubble(a,i):	                #在a[i..n-1]中冒泡最小元素到a[i]位置
    exchange=False
    for j in range(len(a)-1,i,-1):      #无序区元素比较,找出最小元素
      if a[j-1]>a[j]:					#当相邻元素反序时
        a[j],a[j-1]=a[j-1],a[j]         #a[j]与a[j-1]进行交换
        exchange=True			        #本趟排序发生交换置exchange为真
    return exchange                     #返回是否存在交换

#**迭代算法*****************************/
def BubbleSort1(a):	                    #迭代算法：冒泡排序
	for i in range(0,len(a)-1): 		#进行n-1趟排序
		if not Bubble(a,i):return       #本趟未发生交换时结束算法

#***先递后合算法*****************************/
def BubbleSort21(a,i):			    #递归冒泡排序1
    if i==-1:return			        #满足递归出口条件
    BubbleSort21(a,i-1)			    #递归调用
    Bubble(a,i)

def BubbleSort2(a):				    #递归冒泡排序
    BubbleSort21(a,len(a)-2)

#***先合后递算法*****************************/
def BubbleSort31(a,i):
	if i==len(a)-1:return							#满足递归出口条件
	if Bubble(a,i):BubbleSort31(a,i+1)		        #递归调用

def BubbleSort3(a):			#递归冒泡排序2
	BubbleSort31(a,0)

a=[5,4,3,2,1]
#int a[]={2,5,4,1,3};
print("a: ",a)
print("排序")
BubbleSort2(a)
print("a: ",a)
