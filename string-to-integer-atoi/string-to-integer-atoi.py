class Solution:
    def myAtoi(self, s: str) -> int:
        
        res = "0"
        s= s.strip()
        if s == "":
            return 0
        sign = 1
        idx = 0 
        if s[idx] == "-":
            sign = -1
            idx +=1
        elif s[idx] == "+":
            sign = 1
            idx +=1
            
        for i in s[idx:len(s)]:
            if i.isnumeric():
                res+=(i)
            else :
                break
        res = int(res) * sign
        
        if res < -1 * pow(2,31):
            res = -1 * pow(2,31)
        if res > pow(2,31)-1:
            res = pow(2,31)-1
        
        return res