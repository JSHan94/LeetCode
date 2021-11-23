class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > len(nums) or nums[i] < 0 :
                nums[i] = 0
        nums += [0]
        
        for i in range(n):
            nums[nums[i]%(n+1)] += (n+1) 

        for i in range(1,n+1):
            if nums[i] < (n+1) :
                return i
        return n + 1

            
            
            