class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p,g = [0]*n, defaultdict(list)
        p[start] = 1.0
        for idx, (a,b) in enumerate(edges):
            g[a].append((b,idx))
            g[b].append((a,idx))
        heap = []
        heapq.heappush(heap,(-p[start],start))
        
        while heap:
            cur_prob, cur = heapq.heappop(heap)
            if cur == end :
                return -cur_prob
            if g.get(cur) is not None:
                for neighbor,idx in g.get(cur,[]):
                    if p[neighbor] < succProb[idx]*p[cur] : 
                        p[neighbor] = succProb[idx]*p[cur]
                        heapq.heappush(heap,(-p[neighbor],neighbor))
        return 0.0
