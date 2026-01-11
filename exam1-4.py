def MaxMin(a,n):
    maxe,mine=a[0],a[0]
    for i in range(1,n):
        if a[i]>maxe:maxe=a[i]
        elif a[i]<mine:mine=a[i];
    print("maxe=%d,mine=%d"%(maxe,mine))

a=[1,5,3,2,4]
MaxMin(a,len(a))        