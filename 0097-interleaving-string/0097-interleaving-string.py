class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row, col = len(s1), len(s2)
        if row + col != len(s3):
            return False
        
        table = [[False for j in range(col+1)] for i in range(row+1)]
        table[0][0] = True
        for r in range(1,row+1):
            if table[r-1][0] and s1[r-1] == s3[r-1]:
                table[r][0] = True
        for c in range(1, col+1):
            if table[0][c-1] and s2[c-1] == s3[c-1]:
                table[0][c] = True

        for r in range(1,row+1) :
            for c in range(1,col+1):
                if (table[r-1][c]) and (s3[r+c-1] == s1[r-1]):
                    table[r][c] = True
                if (table[r][c-1]) and (s3[r+c-1] == s2[c-1]):
                    table[r][c] = True

        return table[row][col]
        

        
        