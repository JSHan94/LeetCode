class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        climer = 1
        res = 0
        while climer <= n : 
            for i in range(5,0,-1) :
                if climer % (5**i) == 0 :
                    res += i
                    #print("this : ",climer, i)
                    break
            climer +=1
        return res