class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        isPrimes = [1] * n
        isPrimes[0] = 0
        isPrimes[1] = 0
        
        for i in range(2,int(sqrt(n))+1):
            j = 2
            while j*i < n:
                isPrimes[j*i] = 0
                j+=1
        #print(isPrimes)
        return isPrimes.count(1)
            
        