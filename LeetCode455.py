class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()					#默认为递增排序
        s.sort()
        ans=0
        i,j=0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i,ans=i+1,ans+1
            j+=1
        return ans
