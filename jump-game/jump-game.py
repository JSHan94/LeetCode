class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack = [0]
        n = len(nums)
        max_reach = 0
        while stack:
            cur = stack.pop(0)
            if cur == n-1:
                return True
            if cur >= n or nums[cur] + cur <= max_reach:
                continue
            for i in range(max_reach+1,nums[cur]+cur+1):
                if i >=n :
                    break
                stack.append(i)
            max_reach = cur+nums[cur]
                
        return False
            
        