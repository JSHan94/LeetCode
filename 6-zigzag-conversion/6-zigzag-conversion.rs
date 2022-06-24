class Solution:
    def reverse(self, x: int) -> int:
        
        if str(x)[0] == "-":
            res= -int(str(abs(x))[::-1])
        else : 
            res = int(str(abs(x))[::-1])
    
        if res > pow(2,31) or res < pow(-2,31) :
            return 0
        return res