class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def dfs(cur,path):
            if cur == n:
                res.append(path)
                return
            dfs(cur+1, path)
            dfs(cur+1, path + [nums[cur]])
        
        dfs(0,[])
        ans = []
        for i in res :
            if i not in ans:
                ans.append(i)
        return ans