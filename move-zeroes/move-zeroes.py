class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_num = 0
        while 0 in nums:
            nums.remove(0)
            zero_num +=1
            
        for i in range(zero_num):
            nums.append(0)
                
            