def Find(a,n,x):
    i=0
    while i<n:
        if a[i]==x:break
        i+=1
    if i<n:return True
    else:return False

a=[1,5,3,2,4]
print(Find(a,len(a),0))        