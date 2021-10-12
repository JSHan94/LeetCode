class Solution:
    def backtracking(self,nums,path,res):
        if len(nums)==0 and path not in res:
            res.append(path)
        for i in range(len(nums)):
            self.backtracking(nums[:i]+nums[i+1:],path+([nums[i]]),res)
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []                 
        self.backtracking(nums,[],res)
        return res
            
                

        