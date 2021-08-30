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

#         아래와같이 작성하였는데, edges를 매 while마다 루프하는게 문제인듯. heapq.heappush에서 E 만큼의 timecomplexity가 발생할 것이므로 (visit같이 별도로 이미 탐색한 것인지 확인하지 않음). 그렇기 때문에 edge를 enumerate하지말고 그래프를 만들어 dic.get()을 이용하여  O(1)만에 값을 가져와야함
#         p = [0]*n
#         p[start] = 1
#         heap = []
#         heapq.heappush(heap,(-p[start],start))
        
#         while heap:
#             prob, cur = heapq.heappop(heap)
#             if cur == end:
#                 return -prob
#             for idx, (s, d) in enumerate(edges):
#                 neighbor = None
#                 if s == cur:
#                     neighbor = d
#                 elif d == cur :
#                     neighbor = s
#                 else :
#                     continue
                
#                 if p[neighbor] < succProb[idx] * (-prob):
#                     p[neighbor] = succProb[idx] *(-prob)
#                     heapq.heappush(heap,(-p[neighbor],neighbor))
                    
#         return 0.0
