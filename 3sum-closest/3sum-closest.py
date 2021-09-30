class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        gap_res = []
        prev_gap = target - (nums[0]+nums[1]+nums[-1])
        
        for i in range(n-2):
            j,k = i+1, n-1
                       
            while j<k:
                s = nums[i] + nums[j] + nums[k]
                cur_gap = target - s
               
                if abs(prev_gap) <= abs(cur_gap):
                    if abs(target - (nums[i] + nums[j] + nums[k-1]))> abs(target - (nums[i] + nums[j+1] + nums[k])):
                        j+=1
                    else:
                        k-=1
                else:
                    prev_gap = cur_gap
                #print ("prev close:",target - prev_gap, "cur close:",target-cur_gap)
        #print ("prev close:",target - prev_gap)
        return target - prev_gap