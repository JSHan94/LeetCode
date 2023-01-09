class Solution:
    def maximalRectangle(self, m: List[List[str]]) -> int:
        row_n, col_n = len(m), len(m[0])
        res = 0
        h, l, r = [0]*col_n, [0]*col_n, [col_n]*col_n
        for i in range(row_n):
            for j in range(col_n):
                if m[i][j] == "1":
                    h[j] += 1
                else :
                    h[j] = 0
                    
            cur_left, cur_right = 0, col_n
            for j in range(col_n):
                if m[i][j] == "1":
                    l[j] = max(l[j], cur_left )
                else :
                    l[j], cur_left = 0, j+1
            for j in range(col_n-1, -1,-1):
                if m[i][j] == "1":
                    r[j] = min(r[j], cur_right)
                else : 
                    r[j], cur_right = col_n, j
                res = max(h[j] * (r[j]-l[j] ) ,res)
        
        return res
            