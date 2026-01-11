class Solution:
    def minimumTimeRequired(self,_jobs:List[int],_k:int)->int:
        self.ans=0x3f3f3f3f                         #存放最优解
        self.times=[0]*_k
        self.jobs=_jobs
        self.k=_k
        self.dfs(0,0)
        return self.ans

    def dfs(self,ct,i):                         #回溯算法
        if i==len(self.jobs):                       #到达一个叶子结点
            self.ans=ct                                 #求得一个解
        else:
            flag=True
            for j in range(0,self.k):
                if self.times[j]==0:
                    if not flag:return                  #剪支1
                    flag=False
                self.times[j]+=self.jobs[i];            #工作i分配给工人j
                curtime=max(ct,self.times[j])       #剪支2
                if curtime<=self.ans:
                    self.dfs(curtime,i+1)
                self.times[j]-=self.jobs[i]                 #回溯



class Solution:
    def minimumTimeRequired(self,_jobs:List[int],_k:int)->int:
        self.ans=0x3f3f3f3f							#存放最优解
        self.times=[0]*_k
        self.jobs=_jobs
        self.k=_k
       	self.dfs(0,0,0)
        return self.ans

    def dfs(self,cnt,ct,i):							#回溯算法
        if i==len(self.jobs):                 	 	#到达一个叶子结点
            self.ans=ct      							#求得一个解
        else:
            if cnt<self.k:               				 				#优先分配给空闲工人
                self.times[cnt]=self.jobs[i]
                self.dfs(cnt+1,max(self.times[cnt],ct),i+1)
                self.times[cnt]=0										#回溯
            for j in range(0,cnt):				#给已有工作的工人分配
                self.times[j]+=self.jobs[i]
                curtime=max(ct,self.times[j]) 
                if curtime<=self.ans:            						#剪支2
                    self.dfs(cnt,curtime,i+1)						#cnt不变
                self.times[j]-=self.jobs[i] 								#回溯
