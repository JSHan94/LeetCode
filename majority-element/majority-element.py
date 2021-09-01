class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        m = 0
        res = 0
        for i in nums:
            if i not in dic:
                dic[i] = 1                    
            else:
                dic[i] += 1
            
            if dic[i] > m :
                m = dic[i]
                res = i
        
        return res