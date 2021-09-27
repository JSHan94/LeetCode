class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        s,e = 0,0
        n= len(st)
        res = 0
        while s < n:
            target = st[s:e+1]
            if len(target) == len(set(target)) and e < n:
                if len(target)> res:
                    res = len(target)
                e+=1
            else:
                s+=1
                
        return res
                
                