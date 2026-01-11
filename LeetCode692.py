from sortedcontainers import SortedDict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cntmap=SortedDict()
        for i in range(0,len(words)):                           #单词计数存放在cntmap中
            if words[i] in cntmap:cntmap[words[i]]+=1
            else:cntmap[words[i]]=1
        ansmap=SortedDict()
        for s in cntmap.keys():
            cnt=cntmap[s]                                   #获取s对应的计数
            if cnt in ansmap:                           #ansmap中存在该计数
                ss=ansmap[cnt]
                ss.append(s)
                ansmap[cnt]=ss
            else:                       #ansmap中不存在该计数
                ss=[] 
                ss.append(s)
                ansmap[cnt]=ss
        ans=[]
        i=-1					#在ansmap中从后向前查找
        while k>0:           #取前k个字符串存放在ans中
            cnt=ansmap.keys()[i]
            ss=ansmap[cnt]
            for x in ss:
                if k>0:ans.append(x);k-=1
                else:break
            i-=1
        return ans
