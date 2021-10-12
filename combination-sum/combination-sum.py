class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.backtracking(candidates,[],target,res)
        return res 
        
    def backtracking(self,candi,path,target,res):
        if target < 0 :
            return
        elif target == 0 :
            path.sort()
            if path not in res:
                res.append(path)
        else :
            for i in range(len(candi)):
                self.backtracking(candi,path+[candi[i]],target-candi[i],res)