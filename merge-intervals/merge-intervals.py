class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0],x[1]))
        n = len(intervals)
        res = [[intervals[0][0],intervals[0][1]]]
        for item in intervals[1:]:
            if res[-1][1] < item[0]:
                res.append(item)
            else:
                res[-1] = [res[-1][0],max([res[-1][1],item[1]])]
            
    
        return res