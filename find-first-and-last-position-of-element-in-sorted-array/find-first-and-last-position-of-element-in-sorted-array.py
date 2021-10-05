class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 :
            return [-1,-1]

        l,r = 0,len(nums)-1
        
        def binary_l(l,r):
            mid = (l+r)//2
            if l > r :
                return -1
            if target == nums[l]:
                return l
            elif target > nums[mid]:
                return binary_l(mid+1,r)
            elif target <= nums[mid]:
                return binary_l(l+1,mid)
            
        def binary_r(l,r):
            mid = (l+r)//2
            
            if l > r :
                return -1
            if target == nums[r]:
                return r
            elif target >= nums[mid]:
                return binary_r(mid,r-1)
            elif target < nums[mid]:
                return binary_r(l,mid-1)

            
        return [binary_l(l,r), binary_r(l,r)]