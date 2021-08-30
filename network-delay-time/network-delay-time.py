class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d , g = [float('inf')] * (n+1) , defaultdict(list)
        d[0] = 0 
        d[k] = 0
        for (a,b,c) in times :
            g[a].append((b,c))
        
        heap = []
        heapq.heappush(heap,(d[k],k))
        
        while heap :
            dis, cur = heapq.heappop(heap)
            
            for (neighbor, neighborP) in g.get(cur,[]):
                if dis + neighborP < d[neighbor] :
                    d[neighbor] = dis + neighborP
                    heapq.heappush(heap,(d[neighbor],neighbor))
        if max(d[1:]) == float('inf') :
            return -1
        return max(d[1:])
        
        
        
        