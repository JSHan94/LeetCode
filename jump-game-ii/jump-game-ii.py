class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp=[0]+[float('inf')]*(n-1)

        for idx, jump in enumerate(nums):
            for i in range(idx+1,idx+jump+1):
                 if i < n:
                    dp[i] = min(dp[i],dp[idx] + 1)        
        return dp[-1]