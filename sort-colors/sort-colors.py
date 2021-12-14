class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic={0:0,1:0,2:0}
        for n in nums:
            dic[n] += 1

        for i in range(len(nums)) :
            if i< dic[0]:
                nums[i]=0
            if dic[0]<=i < dic[0]+dic[1]:
                nums[i]=1
            if dic[0] + dic[1]<=i < dic[0]+dic[1]+dic[2]:
                nums[i]=2
                
                