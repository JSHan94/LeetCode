class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 :
                    dp[i][j] = grid[i][j]
                if i >= 1 :
                    dp[i][j] = min([dp[i-1][j]+grid[i][j],dp[i][j]])
                if j >= 1:
                    dp[i][j] = min([dp[i][j-1]+grid[i][j],dp[i][j]])
        
        return dp[-1][-1]
                