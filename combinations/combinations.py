class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(cur, path):
            if len(path) == k :
                return res.append(path)
            for i in range(cur,n+1):
                dfs(i+1,path+[i])
            
        
        dfs(1,[])
        return res