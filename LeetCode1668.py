class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n,m=len(sequence),len(word)
        k=1
        subs=word
        while m*k<=n:
            if sequence.find(subs)!=-1:
                k+=1
                subs+=word
            else:break
        return k-1
