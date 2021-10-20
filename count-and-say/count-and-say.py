class Solution:
    def countAndSay(self, n: int) -> str:
        def cas(n):
            res=""
            s = str(n)
            prev=s[0]
            cnt = 0
            for i in s:
                if i != prev:
                    res += str(cnt) + str(prev)
                    cnt = 1
                    prev = i
                else:
                    cnt +=1
            res += str(cnt) + str(prev)
            return int(res)
        
        def recur(n):
            if n == 1:
                return 1
            return cas(recur(n-1))
        
        return str(recur(n))
        
        