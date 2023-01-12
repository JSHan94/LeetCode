class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, len(s)+1):
            # left combination
            if "10"<= s[i-2:i] <= "26":
                dp[i] += dp[i-2]
            # right combination
            if "1" <= s[i-1] <= "9":
                dp[i] += dp[i-1]
                
                
        return dp[-1]