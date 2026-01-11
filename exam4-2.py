def sumk(nums,k):
    ans=[]
    low,high=0,len(nums)-1
    while low<high:
        sum=nums[low]+nums[high]
        if sum<k:low+=1                   				#和太小，向右移动
        elif sum>k:high-=1              				#和太大，向左移动
        else:                          							#找到一个三元组tmp
            tmp=[nums[low],nums[high]]
            ans.append(tmp)           						#将tmp添加到ans中
            low+=1;high-=1
    return ans

a=[1,3,5,7,9,11]
k=12
ans=sumk(a,k)
print("ans=",ans)
