class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        for idx,item in enumerate(intervals):
            if item[0] >= newInterval[0]:
                intervals.insert(idx,newInterval)
                break
            if idx == n-1:
                intervals.append(newInterval)
        res = []
        for item in intervals:
            if not res or item[0] > res[-1][1] :
                res.append(item)
            else:
                res[-1] = [res[-1][0],max([res[-1][1],item[1]])]
        return res