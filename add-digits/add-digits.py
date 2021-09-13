class Solution:
    def addDigits(self, num: int) -> int:
        res = 99
        while res >= 10 :
            res = self.sum_digit(num)
            num = res
        return res
            
    def sum_digit(self,n):
        res = 0 
        while n > 0:
            res += n % 10
            n = n // 10
        #print(res)
        return res    