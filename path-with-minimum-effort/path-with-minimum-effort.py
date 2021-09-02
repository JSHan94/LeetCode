class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dp = [[float('inf') for i in range(len(heights[0]))] for j in range(len(heights))]
        dp[0][0] = 0
        m,n = len(heights), len(heights[0])
        dirX,dirY = [-1,1,0,0], [0,0,1,-1]
        curX,curY = 0,0
        
        heap = []
        heapq.heappush(heap, (0, curX,curY))
        
        while heap:
            maxEffort, curX, curY = heapq.heappop(heap)
            if curX == n-1 and curY == m-1:
                return maxEffort
            for i in range(4):
                newX, newY = curX + dirX[i], curY + dirY[i]

                if 0 <= newX <= n-1 and 0 <= newY <= m-1:
                    effort = abs(heights[curY][curX] - heights[newY][newX])
                    nexteffort = max(effort,dp[curY][curX])
                    if dp[newY][newX] > nexteffort:
                        dp[newY][newX] = nexteffort
                        heapq.heappush(heap,(nexteffort,newX,newY))
                   
        #return dp[n-1][m-1]
            
        
            