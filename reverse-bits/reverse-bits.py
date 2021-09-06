class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # print(1<<2)
        for i in range(32):
            res = res<<1 ^(n&1)
            
            n >>= 1
        return res