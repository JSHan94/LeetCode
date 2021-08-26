class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0 for i in range(n+1)]
        if n == 1:
            return 1
        f[1] = 1
        f[2] = 2
       
        for i in range(3,n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]