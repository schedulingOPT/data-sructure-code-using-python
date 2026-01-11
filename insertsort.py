def Insert(a,i):        #将a[i]有序插入到a[0..i-1]中
    tmp=a[i]
    j=i-1
    while True:             #找a[i]的插入位置
        a[j+1]=a[j]   					#将关键字大于a[i]的元素后移
        j-=1
        if not (j>=0 and a[j]>tmp):
            break           #直到a[j]<=tmp为止 
    a[j+1]=tmp      					#在j+1处插入a[i]

#***迭代算法*****************************
def InsertSort1(a): 		#迭代算法：直接插入排序
    n=len(a)
    for i in range(1,n):
        if a[i]<a[i-1]:Insert(a,i)  #反序时调用Insert

#***先递后合算法*****************************/
def InsertSort21(a,i):       #递归直接插入排序
    if i==0:return
    InsertSort21(a,i-1)
    if a[i]<a[i-1]:Insert(a,i)  #反序时调用Insert

def InsertSort2(a): 		#递归算法：直接插入排序
    InsertSort21(a,len(a)-1)

#***先合后递算法*****************************
def InsertSort31(a,i):   #递归直接插入排序
    n=len(a)
    if i<1 or i>n-1:return
    if a[i]<a[i-1]:Insert(a,i)  #反序时调用Insert
    InsertSort31(a,i+1)

def InsertSort3(a):		#递归算法：直接插入排序
    InsertSort31(a,1);

a=[2,5,4,1,3]
print("a: ",a)
print("排序")
InsertSort3(a)
print("a: ",a)
