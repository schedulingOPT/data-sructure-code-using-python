class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.comp(m-1,n-1)
    def comp(self,x,y):
        a,b=x+y,min(x,y)
        ans=1.0
        while b>0:
            ans*=1.0*a/b
            a-=1;b-=1
        return round(ans)
