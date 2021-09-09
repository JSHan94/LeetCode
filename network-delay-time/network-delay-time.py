class Solution:
    def getindex(self, node,visit):
        minimum = float('inf')
        result = 0
        for idx,item in enumerate(node):
            if (item < minimum) and (idx not in visit):
                result = idx
                minimum = item
        return result

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        visit = []

        p = defaultdict(list)
        for u, v, w in times:
            p[u].append((v, w))
            #p[v].append((u, w))

        node = [float('inf')]*(n+1)
        node[0] = float('inf')
        node[k] = 0

        for _ in range(1,len(node)):
            y = self.getindex(node,visit)
            visit.append(y)
            for v,w in p[y]:
                if v not in visit:
                    node[v] = min(node[v], node[y] + w)
        if max(node[1:]) != float('inf'):
            return(max(node[1:]))
        return -1