class Solution:
    def intToRoman(self, n: int) -> str:
        num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM", "M"]
        
        res = ""
        idx = len(num)-1
        while idx >= 0:
            res += (n // num[idx])*rom[idx]
            n %= num[idx] 
            idx -=1
        
        return res