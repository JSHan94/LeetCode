class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        def check_finish(path):
            for i in range(9):
                for j in range(9):
                    if path[i][j] =='.':
                        return False
            return True
        def rowSafe(r,c,item):
            for i in range(9):
                if self.board[i][c] == item:
                    return False
            return True
        def colSafe(r,c,item):
            for i in range(9):
                if self.board[r][i] == item:
                    return False
            return True
        def boxSafe(r,c,item):
            for k in range(3):
                for l in range(3):
                    n_r,n_c = r - (r%3) + k, c -(c%3) + l
                    if self.board[n_r][n_c] == item:
                        return False
            return True        
            
        def dfs(row,col):
            if check_finish(self.board):
                return True
            if self.board[row][col] != '.':
                if row < 8 :
                    return dfs(row+1,col)
                elif row == 8 :
                    return dfs(0,col+1)
            else : 
                for i in range(1,10):
                    if rowSafe(row,col,str(i)) and colSafe(row,col,str(i)) and boxSafe(row,col,str(i)):
                        self.board[row][col] = str(i)                
                        if dfs(row,col):
                            return True
                    self.board[row][col] = "."
            
       
        dfs(0,0)
        
        return self.board
                
                