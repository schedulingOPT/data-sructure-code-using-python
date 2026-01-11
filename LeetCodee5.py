class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:return s 
        dp=[[False]*n for i in range(n)]        	#二维动态规划数组
        start,maxlength=0,0				#用s[start..start+maxlength-1]表示最长回文子串
        length=1
        while length<=n:             	 	#按长度length枚举区间[i,j]
            i=0
            while i+length-1<n:
                j=i+length-1
                if length==1:                 				#区间中只有一个字符时为回文子串
                    dp[i][j]=True
                elif length==2:                        			#区间长度为2的情况
                    dp[i][j]=(s[i]==s[j])
                else:                                  #区间长度>2的情况
                    dp[i][j]=(s[i]==s[j] and dp[i+1][j-1])
                if dp[i][j] and length>maxlength:           	#求最长的回文子串
                    start=i
                    maxlength=length
                i+=1
            length+=1
        return s[start:start+maxlength]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:return s 
        dp=[[False]*n for i in range(n)]        	#二维动态规划数组
        start,maxlength=0,0				#用s[start..start+maxlength-1]表示最长回文子串
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                length=j-i+1
                if length==1:                 				#区间中只有一个字符时为回文子串
                    dp[i][j]=True
                elif length==2:                        			#区间长度为2的情况
                    dp[i][j]=(s[i]==s[j])
                else:                                  #区间长度>2的情况
                    dp[i][j]=(s[i]==s[j] and dp[i+1][j-1])
                if dp[i][j] and length>maxlength:           	#求最长的回文子串
                    start=i
                    maxlength=length
        return s[start:start+maxlength]
