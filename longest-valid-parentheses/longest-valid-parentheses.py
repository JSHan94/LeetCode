class Solution:

    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        
        if not s :
            return max_len
        stack = [-1]
        for idx,i in enumerate(s) : 
            if i == "(":
                stack.append(idx)
            else :
                stack.pop()
                if stack ==[]:
                    stack.append(idx)
                else:
                    max_len = max(max_len,idx-stack[-1] )
        
        return max_len
        