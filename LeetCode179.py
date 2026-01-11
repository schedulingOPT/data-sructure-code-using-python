import functools
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a=[]
        for x in nums:				#将nums转换为字符串数组a
            a.append(str(x))
        def cmp(s,t):             #按指定方式递减排序
            if s+t<t+s:return 1
            else:return -1
        a.sort(key=functools.cmp_to_key(cmp))
        ans=""
        for i in range(len(a)):ans+=a[i]	#依次合并得到ans
        if ans[0]=='0':return "0"	        #处理特殊情况
        else:return ans
