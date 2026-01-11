def greedly(a):				#贪心算法
    a.sort()				#递增排序
    T,w=0,0					#当前系统总时间和当前作业的等待时间
    for i in range(0,len(a)):           #依次处理各个作业
        T+=a[i]+w
        w+=a[i]
    return T

a=[5,3,4,2]
print("ans=",greedly(a))

