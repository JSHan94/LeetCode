class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m,n = len(heights), len(heights[0])
                
        def bfs(r,c):

            start = [(r,c)]
            q = collections.deque(start)
            dx,dy = [0,0,1,-1], [1,-1,0,0]
            history = [(r,c)]
            while q:
                r,c =q.popleft()
                for i in range(4):
                    new_r,new_c = r+dx[i], c+dy[i]
                    if 0<=new_r<m and 0<=new_c<n and heights[new_r][new_c]>=heights[r][c] and (new_r,new_c) not in history:
                        q.append((new_r,new_c))
                        history.append((new_r,new_c))
            return history
                        
        po,ao=[],[]
        for i in range(n):
            po += bfs(0,i)
            ao += bfs(m-1,i)
        for j in range(m):
            po += bfs(j,0)
            ao += bfs(j,n-1)

        return set(po) & set(ao)
    