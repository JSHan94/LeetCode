class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l,r):
            if l>r:
                return -1
            mid = (l+r) //2
            if target == nums[mid]:
                return mid
            elif nums[mid]>target:
                return binary(l,mid-1)
            else:
                return binary(mid+1,r)
            
        return binary(0,len(nums)-1)
        