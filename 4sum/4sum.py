class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        if n >= 4:
            
            for i in range(n-3):

                for j in range(i+1,n-2):
 
                    k = j+1
                    l = n-1
                    
                    while k < l:
                        cur = nums[i]+nums[j]+nums[k] + nums[l]
                        candi = [nums[i],nums[j],nums[k],nums[l]]
                        if cur == target and candi not in res:
                            res.append(candi)
                        elif cur > target:
                            l -=1
                        else:
                            k +=1
                            
                        
                        
            
        return res