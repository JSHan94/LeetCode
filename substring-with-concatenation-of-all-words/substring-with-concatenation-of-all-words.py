class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        chunk =[]
        n = len(words[0])
        w_n = len(words)
        if n == 1 :
            for i in s:
                chunk.append(i)
        else:
            for idx,i in enumerate(s[:-(n)+1]):
                chunk.append(s[idx:idx+n])
        
        words.sort()
        res = []
        idxx = 0
        while idxx < len(s)-n*w_n+1:
            target = []
            for idx in range(idxx,idxx+n*w_n,n):
                target.append(chunk[idx])
            target.sort()
            if target == words:
                res.append(idxx)    
            idxx +=1
        return res    