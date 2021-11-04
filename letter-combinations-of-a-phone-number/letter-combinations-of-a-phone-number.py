class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num=[0,0,2,3,4,5,6,7,8,9]
        letter_list =  [0,0,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        res = []
        n = len(digits)
        def dfs(pos,path):
            if len(path) == n:
                return res.append(path)
            if pos < n:
                for i in letter_list[int(digits[pos])]:
                    dfs(1+pos, path+i)
                
                
        dfs(0,"")
        return [] if not digits else res
    