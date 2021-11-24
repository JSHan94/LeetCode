class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        self.target = target
        def binary(nums, l,r):
            
            mid = (l+r)//2
            #print(nums,l,mid,r)
            
            if nums[mid] == self.target:
                return mid
            if l >= r :
                return -1


            #if nums[l] <= self.target <= nums[mid]:
            if self.target in nums[l:mid+1]:
                return binary(nums,l,mid)
            else :
                return binary(nums,mid+1,r)
            
        return binary(nums,0,n-1)
            
            
            