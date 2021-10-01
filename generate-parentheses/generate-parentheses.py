class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(open,close,path):
            if len(path) == 2*n :
                res.append(path)
                return
            if open < n:
                backtracking(open+1,close,path+'(')
            if open > close : 
                backtracking(open,close+1,path+')')
        backtracking(0,0,"")
        return res