class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n-2):
            # if nums[i]> 0 :
            #     break
            j , k =i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0 :
                    k-=1
                elif s == 0 :
                    #print("exits")
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    # while j < k and nums[j] == nums[j+1]:
                    #     j+=1
                    # while k > j and nums[k] == nums[k-1]:
                    #     k-=1
                    j+=1
                    # k-=1
                else :
                    j+=1
                        
                        
        return res
                        
            
            