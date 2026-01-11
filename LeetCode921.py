class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]                   #用列表作为栈
        for ch in s:
            if ch=='(':                                     #遇到'('
                st.append(ch)
            else:                                               #遇到')'
                if st and st[-1]=='(': 
                    st.pop()
                else:                                           #栈空或者不匹配的')'进栈
                    st.append(ch)
        return len(st)
