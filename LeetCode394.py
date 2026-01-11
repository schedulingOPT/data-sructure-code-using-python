class Solution:
    def decodeString(self, s: str) -> str:          #求解算法
        self.i=0                                #类变量i从0开始遍历s
        return self.unfold(s)
    
    def unfold(self,s):                                         #递归算法
        ans=""
        while self.i<len(s) and s[self.i]!=']':     #处理到']'为止
            if s[self.i]>='a' and s[self.i]<='z':       #遇到字母
                ans+=s[self.i]; self.i+=1
            else:
                k=0
                while self.i<len(s) and s[self.i]>='0' and s[self.i]<='9': 
                    k=k*10+ord(s[self.i])-ord('0');self.i+=1        #将连续的数字符转换为整数k
                self.i+=1                       #数字符后面为'['，跳过该'['
                tmp=self.unfold(s)                              #返回子串解码结果tmp
                self.i+=1                               #后面是一个']'，跳过该']'
                while k>0:                                      #连接tmp字符串k次
                    ans+=tmp;k-=1
        return ans;                                             #s处理完毕返回ans
