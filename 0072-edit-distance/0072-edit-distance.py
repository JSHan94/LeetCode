class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp table (i,j) means how many ops needs to get word[:i+1] to word[:j+1]
        # so we need to find dp[i][j]
        
        n, m = len(word1), len(word2)
        
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else :
                    delete = dp[i][j-1]
                    insert = dp[i-1][j]
                    replace = dp[i-1][j-1]
                    dp[i][j] = 1 + min(delete, insert, replace)
        return dp[n][m]
                    
        