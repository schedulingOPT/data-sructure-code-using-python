def peaches(n):		#第n天桃子数为1，求第一天桃子数
    ans=1
    for i in range(n-1,0,-1):
        ans=2*(ans+1)
    return ans 

n=10
print("ans:",peaches(n)) 
