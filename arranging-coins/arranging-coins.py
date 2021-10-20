class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 1
        while n >= res*(res+1)//2:
            res +=1
            
        return res-1
            