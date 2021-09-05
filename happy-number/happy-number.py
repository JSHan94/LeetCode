class Solution:
    def isHappy(self, n: int) -> bool:
        li = []
        while True :
            num = 0 
            
            while n>0:
                num += (n%10) * (n%10)
                n = n // 10
                #print(n,num)
            if num == 1 :
                return True
            if num in li : 
                return False
            n = num

            
            li.append(n)
            
    