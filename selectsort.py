def Select(a,i):	#在a[i..n-1]中选择最小元素交换到a[i]位置
    n,minj=len(a),i					#minj表示a[i..n-1]中最小元素的下标
    for  j in range(i+1,n):			#在a[i..n-1]中找最小元素
        if a[j]<a[minj]:minj=j
    if minj!=i:								#若最小元素不是a[i]
      a[minj],a[i]=a[i],a[minj]				#交换
def SelectSort1(a):			#迭代法：简单选择排序
    for  i in range(0,len(a)):		#进行n-1趟排序
        Select(a,i)

#***先递后合算法*****************************/
def SelectSort21(a,i):		#递归的简单选择排序
    if i==-1:return							#满足递归出口条件
    SelectSort21(a,i-1)
    Select(a,i)

def SelectSort2(a):		#递归的简单选择排序
    SelectSort21(a,len(a)-2)

#***先合后递算法*****************************/
def SelectSort31(a,i):		#递归的简单选择排序
    if i==len(a):return							#满足递归出口条件
    Select(a,i)
    SelectSort31(a,i+1)

def SelectSort3(a):			#递归的简单选择排序
    SelectSort31(a,0)

#********************************************/
a=[2,5,4,1,3]
print("a: ",a)
print("排序")
SelectSort3(a)
print("a: ",a)
