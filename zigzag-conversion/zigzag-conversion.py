class Solution:
    def convert(self, s: str, num: int) -> str:
        gap = 2*num -2
        start,end,res = 0,gap,""
        n=len(s)
        if gap == 0:
            return s
        while start < num:
            print("test")
            if start == end or start==0 :
                # +gap
                ts = start
                while ts < n :
                    res += s[ts]
                    ts +=gap
                
            else :
                # start + end 
                ts, te = start,end
                while True:
                    if ts >=n :
                        break
                    res += s[ts]
                    if te >=n :
                        break
                    res += s[te]
                    ts +=gap
                    te +=gap
            
            start+=1
            end -= 1
        return res
                