class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0,-1):
            j = i-1
            if nums[i] > nums[j]:
                idx = i
                t = [item for item in nums[i:] if item > nums[j] ]

                for idxx, item in enumerate(nums[i:]) :
                    if item == min(t):
                        idx += idxx
                        break
                nums[j],nums[idx] = nums[idx],nums[j]
                nums[j+1:] = sorted(nums[j+1:])
                return nums

        return nums.sort()